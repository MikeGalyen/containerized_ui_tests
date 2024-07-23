import pytest

from ..pages.home_page import HomePage

homepage = HomePage()

def test_testing():
    assert True

def test_homepage_exists():
    (homepage
        .go_to_the_homepage()
        .verify_homepage_has_expected_url()
     )