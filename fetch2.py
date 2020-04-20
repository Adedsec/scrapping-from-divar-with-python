from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from phone_getter import get_phone
import get_links
import json

import csv


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
    links = get_links.get(driver, url)
    i = 0
    print(len(links))
    print("---------------------")
    print("---------------------")
    number_list = ['numbers']
    # loop on linkes and get phone number
    for link in links:
        if(i == 0):
            number = get_phone(driver, link, True)
        else:
            number = get_phone(driver, link, False)

        number_list.append(number)
        print(number_list)
        print("---------------------")
        i = i+1
        if i == 5:
            return
    driver.close()


run('https://divar.ir/s/kerman/real-estate')
