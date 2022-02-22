from scrapper.immoweb import ImmowebParser

if __name__ == "__main__":
    url = "https://www.immoweb.be/fr/recherche/maison/a-vendre?countries=BE&geoSearchAreas=s{~tHidi\?lfXlm@j_Nxu@fcGp\ntE`z@rxHbz@n`EvfAxeD`kAx}BxfAxqCbTtY|u@hLxcDuEvq@i`@rsAk`@h`Bkt@djEuEnoAkt@tK_SfkAq`Et\_g@vsAolDdTuYlXiLlXcoAlXo`Eki@yyD?ckCgTesDnG_{@jz@yeDxbAyxMvKmdCfC{iGgCmpBmXesDum@egE{q@ckCav@ohFcv@crM{q@mxCqm@aoAyjCigJ_v@m|Asm@?cTkLujCjLckA_SywA?kX~Rm~@hLgoAl|A{lBtm@_e@d_Duq@taAcTxiBgi@tm@i~@xqCgCp|F{Ojt@eC`cBy`@l|A}d@taAmm@p|Fo\vaAmGzmEw`@`oAgCwm@&hasGarden=true&isALifeAnnuitySale=false&isUnderOption=false&maxPrice=300000&minBedroomCount=2&page=1&orderBy=cheapest"
    
    immowebParse = ImmowebParser()
    homes = immowebParse.scrap(url)
    print(homes)
