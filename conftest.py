import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")
    d = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    yield d
    d.quit()