from time import sleep
import json
import requests
from bs4 import BeautifulSoup
from elasticsearch import Elasticsearch
from phone_getter import get_phone


from selenium import webdriver
pages = 10


def parse(u):
    title = '-'
    rec = {}

    try:
        r = requests.get(u, headers=headers)

        if r.status_code == 200:
            html = r.text
            soup = BeautifulSoup(html, 'lxml')
            # title
            button = soup.select('.post-actions__get-contact')
            title_section = soup.select(
                '.post-page__contact .post-fields-item .post-fields-item__value')

            if title_section:
                title = title_section[0].text

            rec = {'title': title}
    except Exception as ex:
        print('Exception while parsing')
        print(str(ex))
    finally:
        return json.dumps(rec)


if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
        'Pragma': 'no-cache'
    }
    url = 'https://divar.ir/s/kerman/real-estate'
    r = requests.get(url, headers=headers)
    r.encoding = "utf-8"
    print(r.status_code)
    if r.status_code == 200:
        html = r.text
        soup = BeautifulSoup(html, 'lxml')
        links = soup.select('.browse-post-list a')
        print(len(links))
        for link in links:
            # print('https://divar.ir'+link['href'])

            sleep(2)
            result = get_phone('https://divar.ir'+link['href'])
            print(result)
            print('--------------------------')
