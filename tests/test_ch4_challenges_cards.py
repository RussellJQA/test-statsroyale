import pytest
import pytest_check as check

from royale.pages.cards_page import CardsPage
from royale.services import card_service

cards = card_service.get_all_cards()  # list of cards

cards.sort(key=lambda card_element: (card_element.arena, card_element.id))

# CHALLENGE 1: get_card_by_id()
# Write a function that returns a single card given by its Id
#   1. Where would you put this function?
#       ANSWER: In royale.services.card_service. See it there.
#   2. How would you call it in a test?
#       ANSWER: As done below.
#   3. Use a List Comprehension or other means.
#       ANSWER: I used a genrator


@pytest.mark.flaky(reruns=2, reruns_delay=5)
@pytest.mark.parametrize("card_id", (card.id for card in cards))
def test_card_by_id_is_displayed(browser, card_id):
    browser.get("https://statsroyale.com/")

    cards_page = CardsPage(browser).goto()

    api_card = card_service.get_card_by_id(card_id)
    card_on_page = cards_page.get_card_element_by_name(api_card.name)

    check.is_true(card_on_page.is_displayed(),
                  f"Not displayed: card {card_id} ({api_card.name})")


# royale.services.card_service.get_card_by_name() wasn't previously being used.
# So I wrote the test below to demonstrate that it works as expected.
@pytest.mark.flaky(reruns=2, reruns_delay=5)
@pytest.mark.parametrize("card_name", (card.name for card in cards))
def test_card_by_name_is_displayed(browser, card_name):
    browser.get("https://statsroyale.com/")

    cards_page = CardsPage(browser).goto()

    api_card = card_service.get_card_by_name(card_name)
    card_on_page = cards_page.get_card_element_by_name(card_name)

    check.is_true(card_on_page.is_displayed(),
                  f"Not displayed: card {api_card.id} ({card_name})")


# CHALLENGE 2 - api_card.type is different
#   "Ice Spirit" had the type of "Troop" on the Web page.
#   However, the api_card version of "Ice Spirit" instead shows the type
#       as "tid_card_type_character"
#   Fix these errors WITHOUT touching the test methods:
#       Building == tid_card_type_building
#       Spell == tid_card_type_spell
#       Troop == tid_card_type_character
# See class Card in royale.models.card
