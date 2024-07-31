from ..selenium_tools.base_selenium_calls import BaseSeleniumCalls


sel_helper = BaseSeleniumCalls()

class BasePage:

    def go_to_url(self, url):
        sel_helper.navigate_to_url(url)

    def verify_page_has_expected_url(self, url, contains_only=False):
        if contains_only:
            assert url in sel_helper.get_current_page_url()
            return
        assert sel_helper.get_current_page_url() == url

    def verify_element_is_displayed(self, xpath):
        assert sel_helper.check_element_is_displayed(xpath)

    def wait_for_elem_to_be_loaded(self, xpath, wait=30):
        sel_helper.wait_for_element_to_load(xpath, wait=wait)

    def verify_page_title_correct(self, expected_title):
        assert sel_helper.get_tab_title() == expected_title

    def click_locator(self, xpath, wait_time=3):
        element = sel_helper.get_element_by_xpath(xpath)
        sel_helper.wait_for_element_to_be_dispalyed(element, wait_time=wait_time)
        sel_helper.click_page_element(element)

