from selenium.webdriver import ActionChains
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def transfer_button_click(browser: WebDriver, for_upload=False):
    accept_terms = browser.find_element_by_class_name('transfer__button')
    ActionChains(browser).move_to_element(
        accept_terms).click(accept_terms).perform()

    if for_upload:
        waiter(browser, 'spinner__label')


def waiter(browser, class_name, timeout=10):
    WebDriverWait(browser, timeout).until(
        EC.presence_of_element_located(
            (By.CLASS_NAME, class_name))
    )


def better_int(text):
    try:
        return int(text)
    except:
        return(None)
