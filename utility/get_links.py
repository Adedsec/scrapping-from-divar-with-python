from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time


# gets link of agahi s from main url and return alist of links

def get(mydriver, MainLink, count):

    driver = mydriver
    driver.get(MainLink)
    c = (count//20)
    res = []

    for i in range(0, c):
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        print('***** scroll ******')
        time.sleep(2)
        links = []
        posts = driver.find_element_by_css_selector(
            "div.browse-post-list")
        childs = posts.find_elements_by_css_selector("a.kt-post-card")
        #links = [child.get_attribute('href') for child in childs]
        for child in childs:
            links.append(child.get_attribute('href'))
        res.extend(links)

        res = list(dict.fromkeys(res))

    # driver.close()
    return res


# print(get('https://divar.ir/s/kerman/real-estate'))
