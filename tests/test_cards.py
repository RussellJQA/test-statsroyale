# pip installed
import pytest  # installed with webdriver_manager
import pytest_check as check

from royale.pages.cards_page import CardsPage
from royale.pages.card_details_page import CardDetailsPage
from royale.services import card_service

cards = card_service.get_all_cards()  # list of cards

# Make card order deterministic, by sorting them by arena (and then by id).
# Initially, this was done so that arena:0 cards were first in the list.
# [Verified that all api_cards with arena:0 have arena:"Camp" on the Web.]
cards.sort(key=lambda card_element: (card_element.arena, card_element.id))


# If a test initially fails, re-run it up to 2x, with 5 seconds between retries
@pytest.mark.flaky(reruns=2, reruns_delay=5)
@pytest.mark.parametrize("api_card", cards)  # Test all 101 cards
def test_card_is_displayed(browser, api_card):  # Cannon, Earthquake, ...
    browser.get("https://statsroyale.com/")

    cards_page = CardsPage(browser).goto()

    card_on_page = cards_page.get_card_element_by_name(api_card.name)

    check.is_true(card_on_page.is_displayed(),
                  f"Not displayed: card {api_card.id} ({api_card.name})")


@pytest.mark.flaky(reruns=2, reruns_delay=5)
@pytest.mark.parametrize("api_card", cards)
def test_card_details_is_displayed(browser, api_card):
    browser.get("https://statsroyale.com/")

    cards_page = CardsPage(browser).goto()
    cards_page.get_card_element_by_name(api_card.name).click()

    card = CardDetailsPage(browser).get_base_card()

    check.equal(card.name, api_card.name,
                f"Wrong name for card {api_card.id} ({api_card.name})")
    check.equal(card.arena, api_card.arena,
                f"Wrong arena for card {api_card.id} ({api_card.name})")
    check.equal(card.rarity, api_card.rarity,
                f"Wrong rarity for card {api_card.id} ({api_card.name})")
    check.equal(card.type, api_card.type,
                f"Wrong type for card {api_card.id} ({api_card.name})")
