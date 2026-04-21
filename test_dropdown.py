# test_dropdown.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pytest

@pytest.mark.parametrize("option", [
    "Option 1",
    "Option 2"
])
def test_dropdown(driver, option):
    driver.get("https://the-internet.herokuapp.com/dropdown")
    dropdown = Select(driver.find_element(By.ID, "dropdown"))
    dropdown.select_by_visible_text(option)
    assert dropdown.first_selected_option.text == option
