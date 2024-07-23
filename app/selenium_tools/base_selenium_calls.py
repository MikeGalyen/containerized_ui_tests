from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class BaseSeleniumCalls:

    def __init__(self):
        options = webdriver.ChromeOptions()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--window-size=1920,1080')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')
        self.caps = DesiredCapabilities.CHROME
        self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub',
                                       options=options)

    def navigate_to_url(self, url):
        self.driver.get(url)

    def get_current_page_url(self):
        return self.driver.current_url
