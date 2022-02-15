from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium_stealth import stealth

from bs4 import BeautifulSoup

def get_selenium_driver():
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(executable_path='chromedriver', options=options)

    stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )

    return driver


def get_advertisement_links(driver, url):
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    print(soup.prettify())

def main(url):
    driver = get_selenium_driver()
    get_advertisement_links(driver, url)

if __name__ == "__main__":
    url = "https://www.immoweb.be/fr/recherche/maison/a-vendre?countries=BE&geoSearchAreas=s{~tHidi\?lfXlm@j_Nxu@fcGp\ntE`z@rxHbz@n`EvfAxeD`kAx}BxfAxqCbTtY|u@hLxcDuEvq@i`@rsAk`@h`Bkt@djEuEnoAkt@tK_SfkAq`Et\_g@vsAolDdTuYlXiLlXcoAlXo`Eki@yyD?ckCgTesDnG_{@jz@yeDxbAyxMvKmdCfC{iGgCmpBmXesDum@egE{q@ckCav@ohFcv@crM{q@mxCqm@aoAyjCigJ_v@m|Asm@?cTkLujCjLckA_SywA?kX~Rm~@hLgoAl|A{lBtm@_e@d_Duq@taAcTxiBgi@tm@i~@xqCgCp|F{Ojt@eC`cBy`@l|A}d@taAmm@p|Fo\vaAmGzmEw`@`oAgCwm@&hasGarden=true&isALifeAnnuitySale=false&isUnderOption=false&maxPrice=300000&minBedroomCount=2&page=1&orderBy=cheapest"
    main(url)