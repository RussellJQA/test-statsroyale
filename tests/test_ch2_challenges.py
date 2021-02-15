from enum import Enum

# pip installed
import pytest  # installed with webdriver_manager
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

Driver = Enum('Driver', 'CHROME FIREFOX')


def goto_statsroyale_cards():
    driver = webdriver.Chrome(ChromeDriverManager().install())

    # I added, because otherwise "Cards" link doesn't show on my PC
    driver.maximize_window()

    # go to statsroyale.com
    driver.get("https://statsroyale.com/")

    # go to cards page
    driver.find_element(By.CSS_SELECTOR, "[href='/cards']").click()

    return driver


@pytest.mark.flaky(reruns=2, reruns_delay=5)
def test_ice_spirit_is_displayed():
    # Go to statsroyale.com's Cards page
    driver = goto_statsroyale_cards()

    # I added, because otherwise this intermittently fails
    driver.implicitly_wait(10)

    # Assert "Ice Spirit" card is displayed
    card = driver.find_element(By.CSS_SELECTOR, "[href*='Ice+Spirit']")
    assert card.is_displayed()

    driver.quit()


# CHALLENGE 1 - Write another test that asserts that "Lava Golem" is displayed.
# Currently, though, there no longer is a "Lava Golem" card.
# So, test for the "Golem" card (which does currently exist) instead.
@pytest.mark.flaky(reruns=2, reruns_delay=5)
def test_golem_is_displayed():
    # Go to statsroyale.com's Cards page
    driver = goto_statsroyale_cards()

    # I added, because otherwise this intermittently fails
    driver.implicitly_wait(10)

    # Assert "Golem" card is displayed
    card = driver.find_element(By.CSS_SELECTOR, "[href*='Golem']")
    assert card.is_displayed()

    driver.quit()


# CHALLENGE 2 - Write a new test that:
#   1. Unchecks the Common filter at the top
#   2. Asserts that the "Ice Spirit" card is not displayed
@pytest.mark.flaky(reruns=2, reruns_delay=5)
def test_ice_spirit_not_displayed():

    driver = goto_statsroyale_cards()

    # I added, because otherwise element consistently isn't found in time
    driver.implicitly_wait(10)

    # Unselect the "Common" cards checkbox,
    driver.find_element(By.ID, "common-cards").click()

    # Assert that "Ice Spirit" card is not displayed (as it was previously)
    card = driver.find_element(By.CSS_SELECTOR, "[href*='Ice+Spirit']")
    assert not card.is_displayed()

    driver.quit()
