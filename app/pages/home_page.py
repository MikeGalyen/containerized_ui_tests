from .base_page import BasePage
from .page_resources.resources import HomepageResources


class HomePage(BasePage):

    def __init__(self):
        self.resources = HomepageResources()

    def go_to_the_homepage(self):
        self.go_to_url(self.resources.url)
        return self

    def verify_homepage_has_expected_url(self):
        self.verify_page_has_expected_url(self.resources.url)
        return self

    def verify_homepage_title(self):
        self.verify_page_title_correct(self.resources.title)

    def verify_centered_gv_h1_exists(self):
        self.wait_for_elem_to_be_loaded(self.resources.LOCATORS
                                        ["HEADINGS"]
                                        ["H1_HOMEPAGE_TITLE_XPATH"])
        self.verify_element_is_displayed(self.resources.LOCATORS
                                   ["HEADINGS"]
                                   ["H1_HOMEPAGE_TITLE_XPATH"])
        return self

    def verify_gv_nav_button_exists(self):
        self.wait_for_elem_to_be_loaded(self.resources.LOCATORS
                                        ["HEADINGS"]
                                        ["H1_HOMEPAGE_TITLE_XPATH"])
        self.verify_element_is_displayed(self.resources.LOCATORS
                                   ["HEADINGS"]
                                   ["H1_HOMEPAGE_TITLE_XPATH"])
        return self

    def click_twitter_link_in_footer(self):
        self.click_locator(self.resources.LOCATORS
                                        ["NAVIGATION_LINKS"]
                                        ["FOOTER_NAV_LINK_TWITTER"])
        return self




