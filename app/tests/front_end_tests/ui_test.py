from app.pages.home_page import HomePage
from app.pages.external_pages import TwitterPage
#
homepage = HomePage()
twitter = TwitterPage()

def test_homepage_url():
    (homepage
     .go_to_the_homepage()
     .verify_homepage_has_expected_url()
     )

# def test_homepage_tab_title():
#     (homepage
#         .go_to_the_homepage()
#         .verify_homepage_title()
#      )

# def test_gv_navigation_button_works():
#     (homepage
#         .go_to_the_homepage()
#         .
#      )

# def test_locations_navigation_button_work():
#     (homepage
#         .go_to_the_homepage()
#      )
#
# def test_products_navigation_button_work():
#     (homepage
#         .go_to_the_homepage()
#      )
#
# def test_partners_navigation_button_work():
#     (homepage
#         .go_to_the_homepage()
#      )
#
# def test_h1_title_exists():
#     (homepage
#         .go_to_the_homepage()
#         .verify_centered_gv_h1_exists()
#      )

# def test_h1_paragraph_exists():
#     pass
#
# def test_paragraph_section_exists():
#     pass
#
# def test_about_us_link_works():
#     pass
#
# def test_contact_us_link_works():
#     pass
#
# def test_image_figure_exists():
#     pass
#
# def test_apartment_buildings_h3_heading():
#     pass
#
# def test_hotels_h3_heading():
#     pass
#
# def test_special_projects_h3_heading():
#     pass
#
# def test_image_one_exists():
#     pass
#
# def test_image_two_exists():
#     pass
#
# def test_gv_footer_link():
#     pass
#
# def test_about_footer_link():
#     pass
#
# def test_contact_us_footer_link():
#     pass
#
# def test_social_h2():
#     pass
#
# def test_facebook_span():
#     pass
#
# def test_instagram_span():
#     pass

def test_twitter_span():
    assert True
    (homepage
        .go_to_the_homepage()
        .click_twitter_link_in_footer()
     )
    twitter.verify_twitter_redirect_page_has_expected_url()
