class HomepageResources:

    url = "https://guerillavending.com/"
    title = "Guerilla Vending - Boutique curated vending in the DMV Area"# may need adjusting

    LOCATORS = {
        "NAVIGATION_LINKS": {
            "HEADER_MENU_HOMEPAGE_XPATH":
                "//span[contains(@class, 'wp-block-navigation-item__label') and text() = 'Guerilla Vending']",
            "HEADER_MENU_PRODUCTS_XPATH":
                "//span[contains(@class, 'wp-block-navigation-item__label') and text() = 'Products']",
            "HEADER_MENU_PARTNERS_XPATH":
                "//span[contains(@class, 'wp-block-navigation-item__label') and text() = 'Partners']",
            "NAV_GUERILLA_VENDING":
                "//span[contains(@class, 'wp-block-navigation-item__label') and text() = 'Guerilla Vending']",
            "FOOTER_NAV_LINK_TWITTER":
                "//span[contains(@class, 'wp-block-navigation-item__label') and text() = 'Twitter/X']"
        },
        "HEADINGS": {
            "H1_HOMEPAGE_TITLE_XPATH": "//h1[contains(@class, 'has-text-align-center') and text() = 'Guerilla Vending']"
        }

    }

class ContactPageLocators:

    LOCATORS = {
            "": ""
        }

class AboutPageLocators:

    LOCATORS = {
            "": ""
        }

class ExternalResources:

    twitter_url = "https://x.com/"

    LOCATORS = {
        "": ""
    }
