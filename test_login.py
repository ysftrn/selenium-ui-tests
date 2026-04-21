# test_login.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_valid_credentials(driver):
    driver.get("https://the-internet.herokuapp.com/login")
    driver.find_element(By.NAME, "username").send_keys("tomsmith")
    driver.find_element(By.NAME, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    h2 = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, "h2")))
    assert "secure area" in h2.text.lower()

def test_login_invalid_credentials(driver):
    driver.get("https://the-internet.herokuapp.com/login")
    driver.find_element(By.NAME, "username").send_keys("invalidUser")
    driver.find_element(By.NAME, "password").send_keys("wrongPassword")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    error_message = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "flash")))
    assert "invalid" in error_message.text.lower()



