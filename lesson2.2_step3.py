from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Находим числа на странице
    num1_element = browser.find_element(By.ID, "num1")
    num2_element = browser.find_element(By.ID, "num2")

    # Получаем числа и считаем сумму
    num1 = int(num1_element.text)
    num2 = int(num2_element.text)
    total = num1 + num2

    # Находим выпадающий список
    select_element = browser.find_element(By.TAG_NAME, "select")
    select = Select(select_element)

    # Выбираем значение, равное сумме
    select.select_by_value(str(total))

    # Нажимаем кнопку "Submit"
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла