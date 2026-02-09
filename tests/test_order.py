from selenium.webdriver.support.ui import WebDriverWait
import pytest
import allure
from data.test_data import TestDataOrder


@allure.feature("Заказ самоката")
@allure.story("Позитивные сценарии заказа")
class TestOrderScooter:
    
    @pytest.mark.parametrize("order_button_location", ["top", "bottom"], 
                             ids=["top_button", "bottom_button"])
    @pytest.mark.parametrize("test_data", 
                             [TestDataOrder.DATA_SET_1, TestDataOrder.DATA_SET_2],
                             ids=["data_set_1", "data_set_2"])
    @allure.title("Заказ самоката")
    def test_order_scooter_positive(self, main_page, order_page, order_button_location, test_data):
      
        with allure.step(f"1. Нажать кнопку 'Заказать' ({order_button_location})"):
            main_page.click_order_button(order_button_location)
            
        with allure.step("2. Заполнить форму заказа: шаг 1"):
            order_page.fill_step1(
                name=test_data["name"],
                surname=test_data["surname"],
                address=test_data["address"],
                metro_station=test_data["metro"],
                phone=test_data["phone"]
            )
            
        with allure.step("3. Заполнить форму заказа: шаг 2"):
            order_page.fill_step2(
                date=test_data["date"],
                period=test_data["period"],
                color=test_data["color"],
                comment=test_data["comment"]
            )
            
        with allure.step("4. Разместить заказ"):
            order_page.place_order()
            
        with allure.step("5. Проверить успешное оформление"):
            assert order_page.is_order_successful(), "Окно успешного заказа не появилось"
            
        with allure.step("6. Получить номер заказа"):
            order_number = order_page.get_order_number()
            allure.attach(f"Номер заказа: {order_number}", name="Order Info")
            assert "Номер заказа:" in order_number, "Не удалось получить номер заказа"
    
    @allure.title("Проверка редиректа по логотипу Самоката")
    def test_scooter_logo_redirect(self, main_page):
        """
        Тест проверяет редирект по логотипу Самоката
        """
        with allure.step("1. Кликнуть на логотип Самоката"):
            main_page.click_scooter_logo()
            
        with allure.step("2. Проверить URL главной страницы"):
            current_url = main_page.get_current_url()
            expected_url = "https://qa-scooter.praktikum-services.ru/"
            assert current_url == expected_url, \
                f"Ожидался URL: {expected_url}, получен: {current_url}"
    
    @allure.title("Проверка редиректа по логотипу Яндекс")
    def test_yandex_logo_redirect(self, driver, main_page):
        """
        Тест проверяет редирект по логотипу Яндекс
        """
        with allure.step("1. Запомнить текущее окно"):
            original_window = driver.current_window_handle
            
        with allure.step("2. Кликнуть на логотип Яндекс"):
            main_page.click_yandex_logo()
            
        with allure.step("3. Переключиться на новое окно"):
            WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)
            new_window = [window for window in driver.window_handles if window != original_window][0]
            driver.switch_to.window(new_window)
            
        with allure.step("4. Проверить URL страницы Дзен"):
            import time
            time.sleep(2)  # Ждем загрузки
            current_url = driver.current_url
            assert "dzen.ru" in current_url, \
                f"Ожидался переход на Дзен, получен URL: {current_url}"
                
        with allure.step("5. Вернуться в исходное окно"):
            driver.close()
            driver.switch_to.window(original_window)