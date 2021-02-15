from __future__ import annotations

# pip installed
import requests  # installed with webdriver_manager

from royale.models.card import Card


def get_all_cards() -> list[Card]:
    response = requests.get("https://statsroyale.com/api/cards")
    if response.ok:
        return [Card(**card) for card in response.json()]
    raise Exception(
        f"Response was not OK. Status Code: {response.status_code}")


# This wasn't previously called anywhere, so I added a new test which calls it:
#   test_card_by_id_is_displayed() in test_cards_ch4_challenge1.py,
# It's similar to what I did with get_card_by_id (below)
def get_card_by_name(card_name: str) -> Card:
    return next(card for card in get_all_cards() if card.name == card_name)


# For CHAPTER 4 - CHALLENGE 1
def get_card_by_id(card_id: str) -> Card:
    return next(card for card in get_all_cards() if card.id == card_id)
