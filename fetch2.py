from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from phone_getter import get_phone
import get_links


options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.binary_location = "C:/webdrivers/chromedriver.exe"
driver = webdriver.Chrome(ChromeDriverManager().install())

links = get_links.get('https://divar.ir/s/kerman/real-estate')
for link in links:
    number = get_phone(link)
    print(number)
    print("---------------------")
