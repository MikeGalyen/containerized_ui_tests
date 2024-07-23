from ..selenium_tools.base_selenium_calls import BaseSeleniumCalls


class HomePage:

    def __init__(self):
        self.homepage_url = "https://guerillavending.com"
        self.sel_helper = BaseSeleniumCalls()

    def go_to_the_homepage(self):
        self.sel_helper.navigate_to_url(self.homepage_url)
        return self

    def verify_homepage_has_expected_url(self):
        assert self.homepage_url in self.sel_helper.get_current_page_url()
        return self
