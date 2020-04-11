from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time


def get(MainLink):
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--test-type")
    options.binary_location = "C:/webdrivers/chromedriver.exe"
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(MainLink)
    for i in range(0, 2):
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(2)

    posts = driver.find_element_by_xpath(
        "//*[@id='app']/div[2]/main/div[1]/div[2]")
    childs = posts.find_elements_by_css_selector("a.post-card")
    links = [child.get_attribute('href') for child in childs]
    driver.close()
    return links


# print(get('https://divar.ir/s/kerman/real-estate'))
