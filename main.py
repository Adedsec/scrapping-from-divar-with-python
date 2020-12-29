from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import json
import csv
import io
from pathlib import Path
from utility.data_getter import get_data
import utility.get_links
import utility.elastic_config as elastic

# the fetch() gets the data from the base url and prints to console .  first parameter is the base url and second parameter is count of data to fetch


def fetch(url, count):
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
    links = utility.get_links.get(driver, url, count)
    i = 0
    print(len(links))
    print("---------------------")
    print("---------------------")

    es = elastic.connect_elasticsearch()
    # loop on linkes and get phone number
    for link in links:

        data = get_data(driver, link)

        print(data)
        print("---------------------")
        if data != 0:

            rec = json.dumps(data)

            if es is not None:
                if elastic.create_index(es, "divar-scrapping-test1"):

                    out = elastic.store_record(
                        es, "divar-scrapping-test1", rec, data)
                    if out:
                        print('Data indexed successfully')
                        print('**********')
                    print(out)
        i = i+1
        if i == count:
            return
    driver.close()

# example for fetch

#fetch('https://divar.ir/s/tehran', 50)

# the getFromElastic() gets data that stored in elasticsearch server . the first parameter is category (like : "آپارتمان ") second parameter is count of data to get default is 10000 returns list of objects


def getFromElastic(category=None, count=10000):

    if(category != None):
        body = {"query": {"match": {"category": category}}}
    else:
        body = {"query": {"match_all": {}}}

    es = elastic.connect_elasticsearch()
    datas = es.search('divar-scrapping-test1',
                      body=body, size=count)
    res = []

    for data in datas['hits']['hits']:

        res.append(data['_source'])
    return res

# example fpr getFromElasti
#all = getFromElastic()

# the saveToFile() saves data in list that gets from getFromElastic() method in secound parameter and file name in first parameter .  files save in the ResultFiles Directory


def saveToFile(name, list):

    path = "ResultFiles/"
    Path(path).mkdir(parents=True, exist_ok=True)
    fname = path + name
    jsonlist = json.dumps(list, ensure_ascii=False).encode('utf8')
    res = jsonlist.decode()+','
    f = io.open(fname, "a+", encoding="utf-8")
    f.write(res)
    f.close()
    # print(list)

# example fpr saveToFile
#saveToFile('test1.json', getFromElastic(count=20))
