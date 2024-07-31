import logging
from time import perf_counter
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = logging.getLogger(__name__)


class BaseSeleniumCalls:

    def __init__(self):
        pass
        options = webdriver.ChromeOptions()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--window-size=1920,1080')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')
        self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=options)

    def navigate_to_url(self, url):
        self.driver.get(url)

    def get_current_page_url(self):
        return self.driver.current_url

    def get_element_by_xpath(self, xpath):
        return self.driver.find_element(By.XPATH, xpath)

    def check_element_is_displayed(self, xpath):
        try:
            element = self.driver.find_element(By.XPATH, xpath)
            if element.is_displayed():
                return True
            logger.info(f"Element, {element} with xpath, {xpath} exists")
        except Exception as e:
            logger.debug(f"Element with xpath, {xpath} doesn't seem to exist")
            return False

    def wait_for_element_to_load(self, xpath, wait=30):
        start = perf_counter()
        try:
            elem = WebDriverWait(self.driver, wait).until(EC.presence_of_element_located(By.XPATH, xpath))
            end = perf_counter()
            logger.info(f"Element, {elem} from xpath, {xpath} was found in {end - start} seconds")
        except Exception as e:
            end = perf_counter()
            logger.debug(f"Element, from xpath, {xpath} was not detected after {end - start} seconds")

    def wait_for_element_to_be_dispalyed(self, element, wait_time=3):
        wait = WebDriverWait(self.driver, timeout=wait_time)
        wait.until(lambda x: element.is_displayed())

    def get_tab_title(self):
        return self.driver.title

    def click_page_element(self, element):
        element.click()

if __name__ == "__main__":
    x = BaseSeleniumCalls()