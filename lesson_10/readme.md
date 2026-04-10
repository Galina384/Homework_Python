# Проект ДЗ 10

## Запуск тестов с Allure

### 1. Установка зависимостей

pip install selenium pytest allure-pytest
2. Установка Allure

# macOS
brew install allure

# Windows
scoop install allure

# Linux
sudo apt install allure
3. Запуск тестов

pytest test_calculator.py test_ecommerce.py --alluredir=allure_results
4. Формирование и просмотр отчета

allure generate allure_results -o allure_report --clean
allure open allure_report