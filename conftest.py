import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options



@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--width=1920")
    options.add_argument("--height=1080")
    
    
    service = Service(executable_path=r"C:\WebDriver\geckodriver.exe")
    #закоментить строку выше и раскоментить  две ниже на webdriver-manager, чтобы не зависеть от пути к драйверу.
    # from webdriver_manager.firefox import GeckoDriverManager
    # service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service, options=options)
    
    yield driver
    
    driver.quit()


@pytest.fixture
def main_page(driver):
    from pages.main_page import MainPage
    page = MainPage(driver)
    return page.open()


@pytest.fixture
def order_page(driver):
    from pages.order_page import OrderPage
    return OrderPage(driver)
