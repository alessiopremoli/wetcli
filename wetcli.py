import os
from wetcli.files import sanitize_and_check_files
from wetcli.browser import create_browser, destroy_broswer, load_ready_url
from wetcli.utils import transfer_button_click, waiter
from selenium.webdriver import ActionChains


files = sanitize_and_check_files(os.listdir('test_files'))
browser = load_ready_url(create_browser(), 'https://wetransfer.com/')

# 1. COOKIES
try:
    accept_cookie = browser.find_element_by_class_name('welcome__button--accept')
    accept_cookie.click()

    transfer_button_click(browser)
except Exception as e:
    print('ERROR: Accepting cookies', e)
    destroy_broswer(browser)
    quit()

# 2. FORM FILL
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

    destroy_broswer(browser)
    quit()

except Exception as e:
    print('Form Fill error', e)
    destroy_broswer(browser)
    quit()