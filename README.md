Sprint 6: Автотесты для Яндекс.Самокат

## Описание проекта
Автоматизированные тесты для учебного сервиса «Яндекс.Самокат» с использованием:
- Selenium WebDriver
- Page Object Model
- Pytest с параметризацией
- Allure-отчеты

## Структура проекта
Sprint_6/
tests/
  -test_order.py
  -test_questions.py
pages/
  -base_page.py
  -main_page.py
  -order_page.py
locators/
  -main_page_locators.py
  -order_page_locators.py
data/
  -test_data.py
conftest.py
requirements.txt
README.md
.gitignore
urls.py

## Установка
# Установите Firefox браузер
# Установите зависимости
pip install -r requirements.txt

# Установите Allure

# Запуск тестов

# Все тесты
pytest -v

# С Allure отчетом
pytest --alluredir=allure-results
allure serve allure-results

# Только тесты заказа
pytest tests/test_order.py -v

# Только тесты вопросов
pytest tests/test_questions.py -v

# Тестовые сценарии
1.	Вопросы о важном - 8 тестов для выпадающего списка
2.	Заказ самоката - 4 теста (2 точки входа × 2 набора данных)
3.	Проверка логотипов - 2 теста
# Технологии
	Python 3.8+
	Selenium 4
	Pytest
	Allure
	Page Object Model
"# Sprint_6" 
