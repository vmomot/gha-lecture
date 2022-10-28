from pytest import fixture

from config import Config
from allure import step
from src.pages.shop_page import ShopPage


@fixture(scope='session', autouse=True)
def config() -> Config:
    config = Config()
    return config


@fixture
def shop_page(config, page) -> ShopPage:
    with step("Init page"):
        page = ShopPage(base_url=config.base_url, playwright_page=page)
    return page
