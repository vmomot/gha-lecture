import allure


class TestShop:


    @allure.tag("UI")
    @allure.title("The customer can add a product to the cart and checkout it")
    @allure.id("5")
    def test_customer_can_checkout_the_product(self, shop_page):
        shop_page.open()
        shop_page.add_product_to_cart('Cropped Stay Groovy off white')
        shop_page.cart.tap_on_checkout_button()
        shop_page.cart.check_that_checkout_alert_is_present()

    @allure.tag("Stub")
    @allure.description("Test with stub steps to check live documentation")
    @allure.suite("Smoke")
    @allure.story("The customer can add a product to the cart and checkout it")
    @allure.link(url='https://www.youtube.com/watch?v=8QGMjsp8MBU&ab_channel=MarciaLilley',
                 name='Fight!')
    @allure.feature("Checkout")
    @allure.title("Test example")
    @allure.id("6")
    def test_stub(self):
        with allure.step("This is a step"):
            with allure.step("This is a sub-step"):
                with allure.step("This is a sub-sub-step"):
                    with allure.step("This is a assert"):
                        assert True
