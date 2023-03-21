import pytest
from selene.support.shared import browser


@pytest.fixture(scope='package', autouse=True)
def set_browser_resolution():
    browser.config.window_width = 1600
    browser.config.window_height = 1200
