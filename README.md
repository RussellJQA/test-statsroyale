# test-statsroyale

This repository implements the test challenges from Chapters (videos) 1 through 4 of the Kidman Media Group's _Test Automation in Python_ [YouTube playlist](https://www.youtube.com/playlist?list=PLelD030IW7swU6n75wOIeCC9hqKipub_w).

The latter challenges focus on testing the [StatsRoyale.com - Clash Royale Statistics](https://statsroyale.com/) Web site. Some of them use information taken from its [API](https://statsroyale.com/api/cards). They are written using Python, pytest (with a couple of plugins), requests, and Selenium WebDriver.

## Setup Instructions

1. Clone this repository.
2. Download Python 3.7 or higher from [Python.org](https://www.python.org/downloads/), and install it.
3. Set your working directory/folder to the location to which you cloned the repository.
4. Within that directory/folder, install the repository's dependencies:

   - [pytest: simple powerful testing with Python](https://pypi.org/project/pytest/), along with 2 pytest plugins:
   - [pytest-check: pytest plugin that allows multiple failures per test](https://pypi.org/project/pytest-check/)
   - [pytest-rerunfailures: pytest plugin to re-run tests to eliminate flaky failures](https://pypi.org/project/pytest-rerunfailures/)
   - [requests: Python HTTP for Humans](https://pypi.org/project/requests/)
   - [selenium: Python bindings for Selenium](https://pypi.org/project/selenium/)

   from the command line, by typing:

   ```
   pip install -r requirements.txt
   ```

5. Depending on which browser you plan to use for these tests, install the appropriate binary WebDriver file. The tests default to using Chrome, which requires the ChromeDriver WebDriver. Using Firefox requires the GeckoDriver WebDriver. See [INSTALLING-WEBDRIVERS](INSTALLING-WEBDRIVERS.md).

## Some implementation differences between this repository and the referenced videos

1. royale.pages.cards_page.CardsPageMap.card() scrolls the card into view, by calling a 1-line JavaScript script (from Python) :

   ```python
       self._driver.execute_script("arguments[0].scrollIntoView();", element)
   ```

   That's because some cards weren't clickable, because they weren't visible (weren't in view).

2. Uses the [pytest-rerunfailures](https://pypi.org/project/pytest-rerunfailures/) pytest plugin to handle some intermittent test failures on the [StatsRoyale.com](https://statsroyale.com/) Web site. If a test fails, re-runs it up to 2 times, with 5 seconds between retries.

3. Uses soft, non-blocking (delayed) asserts -- as implemented in Brian Okken's [pytest-check](https://pypi.org/project/pytest-check/) pytest plugin -- to handle the multiple assert() statements in tests.test_cards.test_card_details_is_displayed(). See [Non Blocking Assertion Failures with Pytest-check](https://blog.testproject.io/2020/08/11/non-blocking-assertion-failures-with-pytest-check/).

4. Adds a `browser` fixture which:

   - Maximizes the window, because without doing so the Cards link wasn't visible on some PCs. [At the browser's default width, the Cards link was not displayed in the page's header. Instead, it was displayed in a hamburger menu.]
   - Sets an implicit wait using the number of seconds specified by a `config` fixture.
   - Yields a WebDriver instance for the browser (Chrome or Firefox) specified by `config`.

5. Uses the Python 3.9+ capability to type hint tuples, lists, dictionaries, etc. directly. See [PEP 585: Type Hinting Generics In Standard Collections](https://www.python.org/dev/peps/pep-0585/) for more information. Specifically, it replaces:

   ```python
       from typing import Tuple

       def get_card_type_and_arena(self) -> Tuple[str, int]:
   ```

   with:

   ```python
       def get_card_type_and_arena(self) -> tuple[str, int]:
   ```

   and, similarly:

   ```python
       from typing import List

       def get_all_cards() -> List[Card]:
   ```

   with:

   ```python
       def get_all_cards() -> list[Card]:
   ```

   And by adding:

   ```python
       from __future__ import annotations
   ```

   it makes this Python 3.9+ feature available for 3.7 <= Python < 3.9.
