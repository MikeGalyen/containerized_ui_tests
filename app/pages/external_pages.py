from .base_page import BasePage
from .page_resources.resources import ExternalResources


class TwitterPage(BasePage):

    def __init__(self):
        self.resources = ExternalResources()

    def verify_twitter_redirect_page_has_expected_url(self):
        self.verify_page_has_expected_url(self.resources.twitter_url, contains_only=True)
        return self

