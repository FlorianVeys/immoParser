from model.home import Home
from .base import Scrapper


class ImmowebParser(Scrapper):
    def scrap(self, url):
        homes = self.fetch_advertisement_links(url)
        homes = self.hydrate_home()
        return homes

    def fetch_advertisement_links(self, url):
        self.driver.get(url)
        page_content = self.get_page_content()
        mainContent = page_content.find("ul", {"id": "main-content"})
        cards = mainContent.select(".card--result__body")

        homes = []
        for card in cards:
            home = Home()
            home.link = card.select(".card__title-link")[0]['href']
            home.price = card.select(".card--result__price .sr-only")[0].string
            homes.append(homes)

        return homes

    def hydrate_home(self, homes):
        return homes
