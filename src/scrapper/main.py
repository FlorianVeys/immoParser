from scrapper.scrapperFactory import ScrapperFactory

def scrapUrls(urls):
    scrapperFactory = ScrapperFactory()

    homes = set()
    for location, url in urls.items():
        homes.update(scrapperFactory.scrap(url))

    scrapperFactory.close_drivers()

    return homes