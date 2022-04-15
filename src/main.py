from dotenv import load_dotenv
from scrapper.main import scrapUrls

urls = {
    "gembloux": "https://www.immoweb.be/fr/recherche/maison/a-vendre/gembloux/5030?countries=BE&hasGarden=true&isALifeAnnuitySale=false&isUnderOption=false&maxPrice=300000&minBedroomCount=2&page=1&orderBy=cheapest",
    "waremme": "https://www.immoweb.be/fr/recherche/maison/a-vendre/waremme/4300?countries=BE&hasGarden=true&isALifeAnnuitySale=false&isUnderOption=false&maxPrice=300000&minBedroomCount=2&page=1&orderBy=cheapest",
    "helecine": "https://www.immoweb.be/fr/recherche/maison/a-vendre/helecine/1357?countries=BE&hasGarden=true&isALifeAnnuitySale=false&isUnderOption=false&maxPrice=300000&minBedroomCount=2&page=1&orderBy=cheapest",
    "louvain_la_neuve": "https://www.immoweb.be/fr/recherche/maison/a-vendre?countries=BE&hasGarden=true&isALifeAnnuitySale=false&isUnderOption=false&maxPrice=300000&minBedroomCount=2&postalCodes=BE-1348,BE-1340&page=1&orderBy=cheapest",
    "wavre": "https://www.immoweb.be/fr/recherche/maison/a-vendre/wavre/1300?countries=BE&hasGarden=true&isALifeAnnuitySale=false&isUnderOption=false&maxPrice=300000&minBedroomCount=2&page=1&orderBy=cheapest"
}

def application_start():
    load_dotenv()

def application_stop():
    None

if __name__ == "__main__":
    application_start()

    homes = scrapUrls(urls)

    print(homes)

    application_stop()