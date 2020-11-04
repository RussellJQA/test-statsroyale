from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from royale.models.card import Card
from royale.pages.base.pagebase import PageBase


class CardDetailsPage(PageBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.map = CardDetailsPageMap(driver)

    def get_base_card(self) -> Card:
        type_and_arena = self.get_card_type_and_arena()
        return Card(name=self.map.card_name.text,
                    type=type_and_arena[0],
                    arena=type_and_arena[1],
                    rarity=self.map.card_rarity.text.split('\n')[-1],
                    id=None,
                    cost=None,
                    icon=None,
                    hash=None)

    def get_card_type_and_arena(self) -> tuple[str, int]:  # (Troop, Arena 8)
        type_and_arena = self.map.card_category.text.split(', ')
        card_type = type_and_arena[0]  # Troop
        card_arena = type_and_arena[1].split(' ')[-1]  # Arena 8 => 8
        card_arena = 0 if card_arena == 'Camp' else int(card_arena)
        return card_type, int(card_arena)


class CardDetailsPageMap:
    def __init__(self, driver):
        self._driver = driver

    @property
    def card_id(self) -> WebElement:
        return self._driver.find_element(By.CSS_SELECTOR,
                                         "[class*='cardName']")

    @property
    def card_cost(self) -> WebElement:
        return self._driver.find_element(By.CSS_SELECTOR,
                                         "[class*='cardName']")

    @property
    def card_icon(self) -> WebElement:
        return self._driver.find_element(By.CSS_SELECTOR,
                                         "[class*='cardName']")

    @property
    def card_hash(self) -> WebElement:
        return self._driver.find_element(By.CSS_SELECTOR,
                                         "[class*='cardName']")

    @property
    def card_name(self) -> WebElement:
        return self._driver.find_element(By.CSS_SELECTOR,
                                         "[class*='cardName']")

    @property
    def card_category(self) -> WebElement:
        return self._driver.find_element(By.CSS_SELECTOR, "[class*='rarity']")

    @property
    def card_rarity(self) -> WebElement:
        return self._driver.find_element(By.CSS_SELECTOR,
                                         "[class*='rarityCaption']")
