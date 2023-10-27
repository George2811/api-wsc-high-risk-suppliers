from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

def createDriver() -> webdriver.Chrome:
    # Configura el controlador del navegador (en este caso, Chrome)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-web-security")
    chrome_options.add_argument("--disable-site-isolation-trials")
    chrome_options.add_argument("--disable-features=IsolateOrigins,site-per-process")
    
    prefs = {"profile.managed_default_content_settings.images":2}
    chrome_options.headless = True

    chrome_options.add_experimental_option("prefs", prefs)
    myDriver = webdriver.Chrome(options=chrome_options)

    return myDriver

def get_entities(name: str, driver: webdriver.Chrome):
    # Navega a la página web
    url = 'https://projects.worldbank.org/en/projects-operations/procurement/debarred-firms'
    driver.get(url)

    driver.implicitly_wait(8)
    time.sleep(8)

    html = driver.page_source
    soup = BeautifulSoup(html, features="html.parser")

    trs = soup.find_all('tr', {'data-uid': True})

    entities = []
    for tr in trs:
        if(name.lower() in tr.td.text.lower()):
            el = {
                "Firm Name": tr.td.text,
                "Address": tr.contents[2].text,
                "Country": tr.contents[3].text,
                "From Date": tr.contents[4].text,
                "To Date": tr.contents[5].text,
                "Grounds": tr.contents[6].text
            }
            entities.append(el)
    
    hits = len(entities)
       
    return {
        "hits": hits,
        "entities": entities
    }



# <tr class="k-alt" data-uid="9e79c2a8-c20a-41a1-ad0e-3b577f4b3de9" role="row">
#     <td class="" role="gridcell">LONESTAR SUPPLIES AND LOGISTICS (PVT) LTD(AKA AMANI B.P., LTD.)</td>
#     <td class="" role="gridcell">(AKA AMANI B.P., LTD.)</td>
#     <td class="" role="gridcell">LONDON</td>
#     <td class="" role="gridcell">United Kingdom</td>
#     <td class="" role="gridcell">08-Apr-1999</td>
#     <td class="" role="gridcell">Permanent</td>
#     <td class="" role="gridcell">Procurement Guidelines 1.15(a)(ii)</td>
# </tr>
