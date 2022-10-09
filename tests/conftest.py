from pytest import fixture

from config import Config


@fixture(scope='session', autouse=True)
def config() -> Config:
    config = Config()
    return config
