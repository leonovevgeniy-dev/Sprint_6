from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage

class OrderPage(BasePage):
    
     def __init__(self, driver):
        super().__init__(driver)
        
     def fill_step1(self, name, surname, address, metro_station, phone):
        self.send_keys(OrderPageLocators.NAME_INPUT, name)
        self.send_keys(OrderPageLocators.SURNAME_INPUT, surname)
        self.send_keys(OrderPageLocators.ADDRESS_INPUT, address)
        
        metro_field = self.find_element(OrderPageLocators.METRO_INPUT)
        metro_field.click()
        metro_field.send_keys(metro_station)
        
        station_locator = (
                          OrderPageLocators.METRO_STATION[0], 
                          OrderPageLocators.METRO_STATION[1].format(metro_station)
                          )
        self.click_element(station_locator)
        
        self.send_keys(OrderPageLocators.PHONE_INPUT, phone)
        self.click_element(OrderPageLocators.NEXT_BUTTON)
        return self
    
     def select_rental_period(self, period):
        self.click_element(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)
        self.wait.until(EC.presence_of_element_located(
            (By.XPATH, f"//div[@class='Dropdown-option' and text()='{period}']")
        ))
        period_locator = (
            OrderPageLocators.RENTAL_PERIOD_OPTION[0],
            OrderPageLocators.RENTAL_PERIOD_OPTION[1].format(period)
        )
        self.click_element(period_locator)
        
     def fill_step2(self, date, period, color, comment):
        date_input = self.wait.until(EC.element_to_be_clickable(
            OrderPageLocators.DATE_INPUT
        ))
        date_input.click()
        date_input.send_keys(date)
        date_input.send_keys(Keys.ESCAPE)

        self.wait.until(EC.invisibility_of_element_located(
            (By.CLASS_NAME, "react-datepicker")
        ))
        
        rental_field = self.find_element(
            (By.XPATH, "//div[contains(text(), '* Срок аренды')]")
    )
        
        self.scroll_to_element(rental_field)
        
        self.select_rental_period(period)
        
        if color == "black":
            self.click_element(OrderPageLocators.BLACK_CHECKBOX)
        elif color == "grey":
            self.click_element(OrderPageLocators.GREY_CHECKBOX)
        
        self.send_keys(OrderPageLocators.COMMENT_INPUT, comment)
        
     def place_order(self):
        order_button = self.wait.until(EC.element_to_be_clickable(
            OrderPageLocators.ORDER_BUTTON
        ))
        self.scroll_to_element(order_button)
        order_button.click()
        
        self.wait.until(EC.element_to_be_clickable(
            OrderPageLocators.CONFIRM_BUTTON
        )).click()
        
     def is_order_successful(self):
        try:
            success_modal = self.wait.until(EC.visibility_of_element_located(
                OrderPageLocators.SUCCESS_MODAL
            ))
            success_message = self.wait.until(EC.visibility_of_element_located(
                OrderPageLocators.SUCCESS_MESSAGE
            ))
            return success_modal.is_displayed() and success_message.is_displayed()
        except:
            return False
            
     def get_order_number(self):
        order_number_element = self.wait.until(EC.visibility_of_element_located(
            OrderPageLocators.ORDER_NUMBER
        ))
        return order_number_element.text