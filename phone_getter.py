from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

#link = "/v/زمین۷قصبی-شمالی-واگذاری-هوانیروز_زمین-و-کلنگی_کرمان__دیوار/gXKSvqIZ"


def get_phone(mydriver, link, checkrole):
    # options = webdriver.ChromeOptions()
    # options.add_argument('--ignore-certificate-errors')
    # options.add_argument("--test-type")
    # options.binary_location = "C:/webdrivers/chromedriver.exe"
    driver = mydriver
    driver.get(link)

    python_button = driver.find_elements_by_class_name(
        'post-actions__get-contact')[0]
    python_button.click()

    time.sleep(4)

    if (checkrole):
        div = driver.find_elements_by_class_name('divar-modal-footer')[0]
        agree_btn = div.find_element_by_class_name('button')
        agree_btn.click()
        time.sleep(2)
    # type text
    text_area = driver.find_element_by_class_name('post-fields-item__value')
    text = text_area.text
    # driver.close()
    return text


# print(get_phone(link))
