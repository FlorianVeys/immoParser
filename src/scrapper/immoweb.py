import re
from model.home import Home
from .base import Scrapper


class ImmowebParser(Scrapper):
    def scrap(self, url):
        homes = self.__fetch_advertisement_links(url)
        homes = self.__hydrate_home(homes)
        return homes

    def __fetch_advertisement_links(self, url):
        self.driver.get(url)
        page_content = self.get_page_content()
        mainContent = page_content.find("ul", {"id": "main-content"})
        cards = mainContent.select(".card--result__body")

        homes = []
        for card in cards:
            home = Home()
            home.link = self.sanitizer.sanitizeLink(card.select(".card__title-link")[0]['href'].strip())
            home.price = card.select(
                ".card--result__price .sr-only")[0].string.strip()
            homes.append(home)

        return homes

    def __hydrate_home(self, homes):
        for home in homes:
            self.driver.get(home.link)
            page_content = self.get_page_content()

            # Get address
            addresses = page_content.select(
                ".classified__information--address-row")
            for address in addresses:
                home.address += (address.getText()).strip().replace('\n', '')

            # Get description
            description = page_content.select(".classified__description")
            if (len(description) > 0):
                home.description = description[0].getText(
                ).strip().replace('\n', '')

            # Get bedroom and surface
            general_info = page_content.select(
                ".classified__information--property")
            if (len(general_info) > 0):
                general_info_str = ""
                for infos in general_info:
                    general_info_str += (infos.getText()
                                         ).strip().replace('\n', '')
                split_info = general_info_str.split("|")

                if (len(split_info) > 0):
                    home.bedroom_count = re.findall(r'\d+', split_info[0])[0]
                if (len(split_info) > 1):
                    home.land_surface = re.findall(r'\d+', split_info[1])[0]

        return homes
