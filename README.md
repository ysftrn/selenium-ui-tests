# Selenium UI Test Suite

A pytest-based UI test suite built with Selenium WebDriver, targeting [The Internet](https://the-internet.herokuapp.com) — a sandbox application designed for practicing automated testing.

---

## Project Structure

```
selenium-ui-tests/
├── conftest.py         # Shared driver fixture (headless Chrome)
├── test_login.py
├── test_dropdown.py
├── test_checkbox.py
└── test_dynamic_loading.py
```

---

## Scenarios Tested

| File | URL | Scenario |
|---|---|---|
| `test_login.py` | `/login` | Valid and invalid credentials |
| `test_dropdown.py` | `/dropdown` | Option selection via parametrized tests |
| `test_checkbox.py` | `/checkboxes` | State change verification |
| `test_dynamic_loading.py` | `/dynamic_loading/1` | Waiting for dynamically loaded content |

---

## Test Techniques

**Element location** — elements are located using `By.ID`, `By.NAME`, `By.CSS_SELECTOR`, and `By.TAG_NAME` depending on what the DOM provides. CSS selectors are preferred when elements lack unique IDs or names.

**Explicit waits** — `WebDriverWait` with `expected_conditions` is used throughout instead of `time.sleep()`. This makes tests faster and more reliable — execution continues as soon as the condition is met rather than waiting a fixed amount of time.

**State verification** — checkbox tests record initial state before interaction, then assert that state changed after clicking. This is stronger than simply asserting a final state, which could pass even if no interaction occurred.

**Parametrized tests** — `pytest.mark.parametrize` is used for dropdown option selection, running the same test logic against multiple inputs without duplicating test functions.

**Dynamic content** — `EC.text_to_be_present_in_element` is used for content that loads asynchronously, rather than `presence_of_element_located` which only checks if the element exists in the DOM, not whether it contains the expected content.

---

## Design Decisions

**Headless Chrome** — tests run in headless mode via `ChromeDriverManager`, making them suitable for CI environments where no display is available.

**Shared driver fixture with teardown** — the `driver` fixture in `conftest.py` uses `yield` to guarantee `driver.quit()` is called after every test, regardless of pass or fail. This prevents browser instances from being left open on test failure.

**Sandbox target** — The Internet (herokuapp) is used as the test target rather than a real production site. This avoids bot detection, rate limiting, and brittle tests caused by UI changes on live sites.

---

## Running the Tests

**Requirements:**
- Python 3.11+
- Google Chrome

**Install dependencies:**
```bash
pip install selenium pytest webdriver-manager
```

**Run all tests:**
```bash
pytest -v
```

**Run a single file:**
```bash
pytest test_login.py -v
```