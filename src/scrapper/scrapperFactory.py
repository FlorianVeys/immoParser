from .immoweb import ImmowebParser


class ScrapperFactory:
    def __init__(self):
        self.scrappers = {
            "immoweb": ImmowebParser()
        }

    def scrap(self, url):
        isImmowebUrl = url.find("www.immoweb.be") > 0

        if (isImmowebUrl):
            return self.scrappers["immoweb"].scrap(url)

    def close_drivers(self):
        self.scrappers["immoweb"].close_driver()
