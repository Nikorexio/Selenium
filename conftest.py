import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--languages', action='store', default=None,
                     help="Choose language: ru/en/etc")


@pytest.fixture(scope="function")
def browser(request):
    options = Options()
    language = request.config.getoption("languages")
    if language is not None:
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("--languages should be typed")
    yield browser
    print("\nquit browser..")
    browser.quit()
