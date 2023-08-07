import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


@pytest.mark.ui
def test_check_incorrect_username():
    # Створення об'єкту для керування браузером
    driver = webdriver.Chrome(
        service=Service(
            r"/Users/yevheniiamazur/Desktop/projects/mazurQAauto2023project/"
            + "chromedriver"
        )
    )

    # відкриваємо сторінку https://github/login
    driver.get("https://github/login")

    # знаходимо поле в яке будемо вводити неправильне ім'я користувача або поштову адресу
    login_elem = driver.find_element(By.ID, "login_field")

    # вводимо неправильне ім'я користувача або поштову адресу
    login_elem.send_keys("sergiibutenko@mistakeinemail.com")

    # знаходимо поле в яке будемо вводити неправильний пароль
    pass_elem = driver.find_element(By.ID, "password")

    # вводимо неправильний пароль
    pass_elem.send_keys("wrong password")

    # Знаходимо кнопку  Sign In
    btn_elem = driver.find_element(By.NAME, "commit")

    # Емулюємо клік лівою кнопкою мишки
    btn_elem.click()

    # Перевіряємо що назва сторінки така: яку ми очікуємо
    assert driver.title == "Sign in to GitHub - GitHub"

    # закриваємо браузер
    driver.close()
