from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from royale.pages.base.pagebase import PageBase


class CardsPage(PageBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.map = CardsPageMap(driver)

    def goto(self):
        self.headernav.goto_cards_page()
        return self

    def get_card_element_by_name(self, card_name: str) -> WebElement:

        # Ice Spirit => Ice+Spirit
        #   or
        # Lava Golem => Lava+Golem

        if ' ' in card_name:
            card_name = card_name.replace(' ', '+')
        return self.map.card(card_name)


class CardsPageMap:
    def __init__(self, driver):
        self._driver = driver

    def card(self, card_name) -> WebElement:
        element = self._driver.find_element(By.CSS_SELECTOR,
                                            f"[href*='{card_name}']")
        # I added this, because some cards couldn't be clicked because
        # they weren't visible (in view).
        self._driver.execute_script("arguments[0].scrollIntoView();", element)
        return element
