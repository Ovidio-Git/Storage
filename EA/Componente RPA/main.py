from typing import Text
from selenium import webdriver
from toolbox  import URLS
from toolbox  import XPATH_NUM_DOWNLOADS
from toolbox  import XPATH_NUM_QUERIES
from toolbox  import API_HOST
from datetime import datetime
from selenium.webdriver.chrome.options import Options
import requests



def loadStatistics(queries, downloads, date):
    dataResponse = [] 
    for i in range(len(queries)):
        dataResponse.append({
                        "numeroconsultas":queries[i].replace('.',''),
                        "numerodescargas":downloads[i].replace('.',''),
                        "idconjunto":i+1,
                        "fecha":date
                    })
    p = requests.post(f'http://{API_HOST}/api/estadisticas/', json=dataResponse)
    print('RESPONSE RESPONSE RESPONSE RESPONSE RESPONSE RESPONSE')
    print(p.text)
    #print(dataResponse)

def Run():
    chromeOptions = Options()
    chromeOptions.add_argument('--headless')
    browser = webdriver.Chrome('chromedriver', chrome_options=chromeOptions)
    numDownloadsValue = []
    numQueriesValue   = []
    for url in URLS:
        browser.get(url)
        numDownloadsElement = browser.find_element_by_xpath(XPATH_NUM_DOWNLOADS)
        numQueriesElement   = browser.find_element_by_xpath(XPATH_NUM_QUERIES)
        numDownloadsValue.append(numDownloadsElement.text)
        numQueriesValue.append(numQueriesElement.text)
    dateToday = datetime.now()
    dateToday = str(dateToday)
    loadStatistics(numQueriesValue, numDownloadsValue, dateToday)
    browser.close()

if __name__ == '__main__':
    Run()
