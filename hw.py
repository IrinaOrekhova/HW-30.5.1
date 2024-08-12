from selenium.webdriver.support import expected_conditions as EC
import pytest
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(autouse=True)
def driver():
    driver = webdriver.Chrome()
    # Переходим на страницу авторизации
    driver.get('https://petfriends.skillfactory.ru/login')
    driver.maximize_window()
    yield driver

    driver.quit()

    """явное ожидание"""

def test_show_my_pets(driver):
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'email')))
    driver.find_element(By.ID, 'email').send_keys('rogonova.irina@bk.ru')
    driver.find_element(By.ID, 'pass').send_keys('Q7,tegmy')
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    assert driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"


    """неявное ожидание"""

def test_show_my_pets2(driver):
    driver.find_element(By.ID, 'email').send_keys('Ваша почта')
    driver.find_element(By.ID, 'pass').send_keys('ваш пароль')
    driver.implicitly_wait(10)
    visible_button = (By.CSS_SELECTOR, 'button[type="submit"]')
    driver.find_element(*visible_button).click()
    assert driver.find_element(By.TAG_NAME, 'h1').text == 'PetFriends'