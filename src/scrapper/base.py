from abc import ABC, abstractmethod

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium_stealth import stealth
from bs4 import BeautifulSoup


class Scrapper(ABC):
    def __init__(self):
        self.driver = self.__construct_selenium_driver()
        super().__init__()

    def close_driver(self):
        self.driver.close()
        self.driver.quit()

    def __construct_selenium_driver(self):
        options = Options()
        options.headless = True
        driver = webdriver.Chrome(
            executable_path='chromedriver', options=options)

        stealth(
            driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
        )
        return driver

    def get_page_content(self):
        return BeautifulSoup(self.driver.page_source, 'html.parser')

    @abstractmethod
    def scrap(self, url):
        pass
