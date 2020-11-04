from royale.pages.headernav import HeaderNav


class PageBase:
    def __init__(self, driver):
        self.headernav = HeaderNav(driver)
