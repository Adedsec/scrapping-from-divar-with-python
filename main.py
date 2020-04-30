from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import json
import csv

from utility.data_getter import get_data
import utility.get_links
import utility.elastic_config as elastic


def run(url):
    # Driver setup
    options = webdriver.ChromeOptions()
    prefs = {'profile.default_content_setting_values': {'images': 2,
                                                        'ssl_cert_decisions': 2
                                                        }}
    options.add_experimental_option('prefs', prefs)
    options.add_argument("start-maximized")
    options.add_argument("--disable-extensions")
    driver = webdriver.Chrome(
        options=options, executable_path="C:\\webdrivers\\chromedriver.exe")

    # getting links list
    links = utility.get_links.get(driver, url)
    i = 0
    print(len(links))
    print("---------------------")
    print("---------------------")

    es = elastic.connect_elasticsearch()
    # loop on linkes and get phone number
    for link in links:
        if(i == 0):
            data = get_data(driver, link, True)
        else:
            data = get_data(driver, link, False)

        print(data)
        print("---------------------")
        if data != 0:

            rec = json.dumps(
                {'number': data['number'], 'category': data['category'], 'main-category': data['main-category'], 'title': data['title']})

            if es is not None:
                if elastic.create_index(es, "scrapping"):
                    out = elastic.store_record(
                        es, "divar-scrapping", rec, my_id=data['number'])
                    print('Data indexed successfully')
                    print('**********')
                    print(out)
        i = i+1
        if i == 6:
            return
    driver.close()


run('https://divar.ir/s/kerman')
