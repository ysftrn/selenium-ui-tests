import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

# LOCAL TESTING
# @pytest.fixture
# def driver():
#     options = Options()
#     options.add_argument("--headless")
#     d = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#     yield d
#     d.quit()



# REMOTE TESTING (VIA DOCKER)
@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")
    d = webdriver.Remote(
        command_executor="http://localhost:4444",
        options=options
    )
    yield d
    d.quit()