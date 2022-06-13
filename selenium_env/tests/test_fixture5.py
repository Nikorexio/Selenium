import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(7)
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('links', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1",
                                   "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1",
                                   "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1",
                                   "https://stepik.org/lesson/236904/step/1",
                                   "https://stepik.org/lesson/236905/step/1"])
def test_guest_should_see_login_link(browser, links):
    link = links
    browser.get(link)
    input1 = browser.find_element(By.CSS_SELECTOR, ".quiz-component > textarea")
    answer = math.log(int(time.time()))
    input1.send_keys(str(answer))
    browser.find_element(By.CSS_SELECTOR, ".submit-submission").click()
    text = browser.find_element(By.CSS_SELECTOR, ".smart-hints__hint").text

    assert text == "Correct!", text
