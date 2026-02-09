from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from locators.order_page_locators import OrderPageLocators
import time
from selenium.webdriver.common.keys import Keys


class OrderPage:
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        
    def fill_step1(self, name, surname, address, metro_station, phone):
        self.wait.until(EC.element_to_be_clickable(
            OrderPageLocators.NAME_INPUT
        )).send_keys(name)
        
        self.driver.find_element(*OrderPageLocators.SURNAME_INPUT).send_keys(surname)
        
        self.driver.find_element(*OrderPageLocators.ADDRESS_INPUT).send_keys(address)
        
        metro_field = self.driver.find_element(*OrderPageLocators.METRO_INPUT)
        metro_field.click()
        metro_field.send_keys(metro_station)
        
        station_locator = (OrderPageLocators.METRO_STATION[0], 
                          OrderPageLocators.METRO_STATION[1].format(metro_station))
        self.wait.until(EC.element_to_be_clickable(station_locator)).click()
        
        self.driver.find_element(*OrderPageLocators.PHONE_INPUT).send_keys(phone)
        
        self.driver.find_element(*OrderPageLocators.NEXT_BUTTON).click()
    
    def select_rental_period(self, period):
        dropdown = self.driver.find_element(*OrderPageLocators.RENTAL_PERIOD_DROPDOWN)
        dropdown.click()
        time.sleep(1)
        
        option_xpath = f"//div[@class='Dropdown-option' and text()='{period}']"
        option = self.driver.find_element(By.XPATH, option_xpath)
        
        option.click()
        time.sleep(0.5)
        
    def fill_step2(self, date, period, color, comment):
        date_input = self.wait.until(EC.element_to_be_clickable(
            OrderPageLocators.DATE_INPUT
        ))
        date_input.click()
        date_input.send_keys(date)
        date_input.send_keys(Keys.ESCAPE)
        time.sleep(1)
        
        rental_field = self.driver.find_element(
            By.XPATH, "//div[contains(text(), '* Срок аренды')]"
        )
        
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", rental_field)
        time.sleep(0.5)
        
        self.select_rental_period(period)
        
        if color == "black":
            self.driver.find_element(*OrderPageLocators.BLACK_CHECKBOX).click()
        elif color == "grey":
            self.driver.find_element(*OrderPageLocators.GREY_CHECKBOX).click()
        
        comment_input = self.driver.find_element(*OrderPageLocators.COMMENT_INPUT)
        comment_input.clear()
        comment_input.send_keys(comment)
        
    def place_order(self):
        order_button = self.wait.until(EC.element_to_be_clickable(
            OrderPageLocators.ORDER_BUTTON
        ))
        self.driver.execute_script("arguments[0].scrollIntoView();", order_button)
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