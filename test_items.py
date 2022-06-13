from selenium.webdriver.common.by import By
import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_should_open_with_user_language_and_there_is_add_to_basket_btn(browser):
    browser.get(link)
    time.sleep(5)
    button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")

    assert button is not None
