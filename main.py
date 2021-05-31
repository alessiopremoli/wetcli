import os
from utils import transfer_button_click, waiter
from selenium.webdriver import ActionChains
from browser import destroy_broswer, create_browser, load_ready_url


files = ['test_files/uploadtest.txt', 'test_files/uploadtest2.log']
# TODO: unique file name check, file exists, 2GB max


browser = load_ready_url(create_browser(), 'https://wetransfer.com/')

# 1. Handling cookies
try:
    accept_cookie = browser.find_element_by_class_name('welcome__button--accept')
    accept_cookie.click()

    transfer_button_click(browser)
except Exception as e:
    print('ERROR: Accepting cookies', e)

# 2. Form fill

try:
    # 2.1 LINK ONLY
    browser.find_element_by_class_name('transfer__toggle-options').click()

    radio_link = browser.find_element_by_css_selector("input[type='radio'][name='transfer__type-link']")
    ActionChains(browser).move_to_element(radio_link).click(radio_link).perform()

    browser.find_element_by_class_name('transfer__toggle-options').click()

    # 2.2 FILL MESSAGE
    message = browser.find_element_by_name('message')
    message.send_keys('Test Message')

    # 2.3 ADD FILE
    for file in files:
        browser.find_element_by_css_selector("input[type='file']").send_keys(os.getcwd() + f'/{file}')

    transfer_button_click(browser, for_upload=True)

    print('Uploading...')
    waiter(browser, class_name='transfer-link__url', timeout=5 * 60)

    link = browser.find_element_by_class_name('transfer-link__url').get_attribute('value')
    print('GENERATED URL:')
    print(f'{link}')


except Exception as e:
    print('Form Fill error', e)