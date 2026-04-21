from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_checkbox(driver):
    driver.get("https://the-internet.herokuapp.com/checkboxes")
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#checkboxes input[type='checkbox']"))
    )
    checkboxes = driver.find_elements(By.CSS_SELECTOR, "#checkboxes input[type='checkbox']")
    checkbox1 = checkboxes[0]
    checkbox2 = checkboxes[1]

    checkbox1_initial_status = checkbox1.is_selected()
    checkbox2_initial_status = checkbox2.is_selected()

    checkbox1.click()
    checkbox2.click()

    checkbox1_final_status = checkbox1.is_selected()
    checkbox2_final_status = checkbox2.is_selected()

    assert checkbox1_final_status != checkbox1_initial_status
    assert checkbox2_final_status != checkbox2_initial_status


