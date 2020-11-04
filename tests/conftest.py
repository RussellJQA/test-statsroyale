"""
This module contains shared fixtures.
"""

import json
from pathlib import Path

import pytest
import selenium.webdriver


# scope="session" means "Run fixture 1x per session"
# (1x before entire test suite)
@pytest.fixture
def config(scope="session"):
    # NOTE: pytest --fixtures test_cards.py lists its available fixtures
    # A docstring (as below) for the fixture will be included in the list
    """Load/update configuration parameters to pass to WebDriver instance"""

    # Read the file
    with open(Path("tests") / "config.json") as config_file:
        config = json.load(config_file)

    # Assert values are acceptable
    assert config["browser"] in ["Firefox", "Chrome"]
    assert isinstance(config["implicit_wait"], int)
    assert config["implicit_wait"] > 0

    # Return config so it can be used
    return config


# scope="function" [the default] means "Run fixture 1x for each test case" )"
@pytest.fixture
def browser(config):
    """Yield WebDriver instance with the specified configuattion"""

    # Setup
    #   This section known as Arrange (in the Arrange-Act-Assert paradigm)
    #   This section known as Given (in the Given-When-Then paradigm)

    # Initialize the WebDriver instance
    if config["browser"] == "Chrome":
        b = selenium.webdriver.Chrome()

    elif config["browser"] == "Firefox":
        b = selenium.webdriver.Firefox()

    else:
        raise Exception(f'Browser "{config["browser"]}" is not supported')

    b.maximize_window()  # Needed so that searched-for elements are visible

    # Wait up to specified number of seconds for elements to appear
    b.implicitly_wait(config["implicit_wait"])

    # Run the test: Return the WebDriver instance for the test
    #   This section known as Act (in the Arrange-Act-Assert paradigm)
    #   This section known as When (in the Given-When-Then paradigm)

    yield b

    # Teardown/Cleanup

    # Quit the WebDriver instance for the cleanup
    b.quit()
