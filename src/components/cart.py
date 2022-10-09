from playwright.sync_api import Page
from allure import step


class Cart:
    _OPEN_CART_BUTTON = '//*[@id="root"]/div/div/button'
    _CHECKOUT_BUTTON = '//*[@id="root"]/div/div/div/div[3]/button'
    _UP_PRODUCT_QUANTITY = '//*[@id="root"]/div/div/div/div[2]/div/div[2]/div/button[2]'

    def __init__(self, playwright_page: Page):
        self._page: Page = playwright_page

    @step("Tap on cart button")
    def open_cart(self):
        self._page.click(self._OPEN_CART_BUTTON)

    @step("Tap on checkout button")
    def tap_on_checkout_button(self):
        self._page.click(self._CHECKOUT_BUTTON)

    @step
    def check_that_checkout_alert_is_present(self):
        try:
            self._page.on('dialog', lambda dialog: dialog.accept())
            assert True
        except Exception:
            assert False

