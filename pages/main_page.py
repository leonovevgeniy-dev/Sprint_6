from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from locators.main_page_locators import MainPageLocators
import time

class MainPage: 
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        
    def open(self):
        self.driver.get("https://qa-scooter.praktikum-services.ru/")
        self.wait.until(EC.visibility_of_element_located(MainPageLocators.HEADER))
        return self
    
    def get_order_button(self, button_type='top'):
        if button_type == 'top':
            return self.wait.until(EC.element_to_be_clickable(
                MainPageLocators.ORDER_BUTTON_TOP
            ))
        else:
            bottom_button = self.driver.find_element(*MainPageLocators.ORDER_BUTTON_BOTTOM)
            self.driver.execute_script("arguments[0].scrollIntoView();", bottom_button)
            return self.wait.until(EC.element_to_be_clickable(
                MainPageLocators.ORDER_BUTTON_BOTTOM
            ))
    
    def click_order_button(self, button_type='top'):
        button = self.get_order_button(button_type)
        button.click()
        
    def click_question(self, question_index):
        questions_section = self.driver.find_element(*MainPageLocators.QUESTIONS_SECTION)
        
        self.driver.execute_script("arguments[0].scrollIntoView(true);", questions_section)
        
        time.sleep(0.5)
        
        question = self.driver.find_element(*MainPageLocators.QUESTION_HEADERS[question_index])
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
        
    def get_current_url(self):
        return self.driver.current_url