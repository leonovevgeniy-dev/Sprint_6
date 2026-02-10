from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from urls import MAIN_PAGE_URL

class MainPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver, url=MAIN_PAGE_URL)
        
    def open(self):
        return super().open()
    
    def get_order_button(self, button_type='top'):
        if button_type == 'top':
            return self.wait.until(EC.element_to_be_clickable(
                MainPageLocators.ORDER_BUTTON_TOP
            ))
        else:
            bottom_button = self.find_element(MainPageLocators.ORDER_BUTTON_BOTTOM)
            self.scroll_to_element(bottom_button)
            return self.wait.until(EC.element_to_be_clickable(
                MainPageLocators.ORDER_BUTTON_BOTTOM
            ))
    
    def click_order_button(self, button_type='top'):
        button = self.get_order_button(button_type)
        button.click()
        
    def click_question(self, question_index):
        questions_section = self.find_element(MainPageLocators.QUESTIONS_SECTION)
        self.scroll_to_element(questions_section)
        
        self.wait.until(EC.element_to_be_clickable(
            MainPageLocators.QUESTION_HEADERS[question_index]
        ))
        
        question = self.find_element(MainPageLocators.QUESTION_HEADERS[question_index])
        self.driver.execute_script("arguments[0].click();", question)
        
    def get_answer_text(self, question_index):
        answer = self.wait.until(EC.visibility_of_element_located(
            MainPageLocators.QUESTION_ANSWERS[question_index]
        ))
        return answer.text
    
    def click_scooter_logo(self):
        logo = self.wait.until(EC.element_to_be_clickable(
            MainPageLocators.SCOOTER_LOGO
        ))
        logo.click()
        
    def click_yandex_logo(self):
        logo = self.wait.until(EC.element_to_be_clickable(
            MainPageLocators.YANDEX_LOGO
        ))
        logo.click()
        