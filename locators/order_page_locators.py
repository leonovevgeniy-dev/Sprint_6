from selenium.webdriver.common.by import By


class OrderPageLocators:
    """Локаторы страницы заказа"""
    
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_STATION = (By.XPATH, "//div[text()='{}']")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    DATE_PICKER_DAY = (By.XPATH, "//div[contains(@class, 'react-datepicker__day') and not(contains(@class, 'outside-month'))]")
    
    RENTAL_PERIOD_DROPDOWN = (By.CLASS_NAME, "Dropdown-control")

    RENTAL_PERIOD_OPTION = (By.XPATH, "//div[@class='Dropdown-option' and text()='{}']")
    
    BLACK_CHECKBOX = (By.ID, "black")
    GREY_CHECKBOX = (By.ID, "grey")
    
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    
    ORDER_BUTTON = (By.XPATH, "(//button[text()='Заказать'])[2]")
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")

    SUCCESS_MODAL = (By.CLASS_NAME, "Order_Modal__YZ-d3")
    SUCCESS_MESSAGE = (By.XPATH, "//div[text()='Заказ оформлен']")
    ORDER_NUMBER = (By.CLASS_NAME, "Order_Text__2broi")