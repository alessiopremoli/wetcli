from utils import waiter
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.webdriver import WebDriver


def create_browser(headless=True):
    opts = Options()
    opts.headless = headless

    browser = Firefox(options=opts)

    return browser


def load_ready_url(browser: WebDriver, url: str):
    browser.get(url)
    waiter(browser, 'welcome__cookie-notice')

    return browser



def destroy_broswer(browser: WebDriver):
    browser.close()
