from selenium import webdriver


__all__ = [
    'get_chrome_driver'
]


def get_chrome_driver(chrome_debug=False):
    driver_path = '/usr/local/bin/chromedriver'
    options = webdriver.ChromeOptions()
    if chrome_debug == False:
        options.add_argument('headless')
        options.add_argument('window-size=1920x1080')
        options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(
        executable_path=driver_path,
        chrome_options=options,
        service_args=['--silent'],
        service_log_path='./chrome.log'
    )
    driver.maximize_window()
    return driver
