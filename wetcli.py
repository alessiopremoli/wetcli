#!/Users/macbookpro/code/alessiopremoli/wet_cli/env/bin/python
import os, sys, argparse
from wetcli_utils.files import sanitize_and_check_files
from wetcli_utils.browser import create_browser, destroy_broswer, load_ready_url
from wetcli_utils.utils import Modes, transfer_button_click, waiter
from selenium.webdriver import ActionChains
    

def wet_cli(mode, upload_message, dir_path=None, file_path=None):  

    print(file_path)

    files = []
    if mode == Modes.DIRECTORY:
        files = os.listdir(dir_path)
    elif mode == Modes.FILE:
        files = [file_path]
    else:
        raise Exception('No valid option provided')


    files = sanitize_and_check_files(files, dir_path)
    browser = load_ready_url(create_browser(), 'https://wetransfer.com/')
    print('Uploading...')


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
        message.send_keys(upload_message)

        # 2.3 ADD FILE
        for file in files:
            joined_path = os.path.join(dir_path, file) if dir_path else file 
            browser.find_element_by_css_selector("input[type='file']").send_keys(joined_path)

        transfer_button_click(browser, for_upload=True)

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


# REAL CLI
sys.tracebacklimit = 0
default_message = 'Uploaded using WETCLI, a cli for getting wetransfer links => https://github.com/alessiopremoli/wetcli'

wetcli_parser = argparse.ArgumentParser(prog='wetcli', description='WETCLI: a cli for getting wetransfer links')

wetcli_parser.add_argument('-d', action='store',type=str, help='path of the folder to upload', default=None)
wetcli_parser.add_argument('-f', action='store',type=str, help='file to be uploaded', default=None)
wetcli_parser.add_argument('-m', action='store',type=str, help='file to be uploaded', default=default_message)

args = wetcli_parser.parse_args()
dir_path = args.d
file_path = args.f
message=args.m


if dir_path:
    if not os.path.isdir(dir_path):
        raise Exception('No valid path provided')
    wet_cli(mode=Modes.DIRECTORY, dir_path=os.path.abspath(dir_path), upload_message=message)
elif file_path:
    if not os.path.exists(file_path):
        raise Exception('No valid file path provided')
    wet_cli(mode=Modes.FILE, file_path=os.path.abspath(file_path), upload_message=message)
else:
    raise Exception('No valid option provided')
