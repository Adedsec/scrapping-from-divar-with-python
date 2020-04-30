from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

#link = "/v/زمین۷قصبی-شمالی-واگذاری-هوانیروز_زمین-و-کلنگی_کرمان__دیوار/gXKSvqIZ"


def get_data(mydriver, link, checkrole):
    # options = webdriver.ChromeOptions()
    # options.add_argument('--ignore-certificate-errors')
    # options.add_argument("--test-type")
    # options.binary_location = "C:/webdrivers/chromedriver.exe"
    driver = mydriver
    driver.get(link)

    python_button = driver.find_elements_by_class_name(
        'post-actions__get-contact')[0]
    python_button.click()
    main_category_field = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div/div[1]/div/div/div[3]/a')

    main_category = main_category_field.get_attribute('title')

    category_field = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div/div[1]/div/div/div[last()]/a')
    category = category_field.get_attribute('title')

    title_section = driver.find_element_by_xpath(
        '//*[@id="app"]/div[2]/div/div[3]/div[1]/div[1]/h1')

    title = title_section.text

    time.sleep(4)

    if (checkrole):
        div = driver.find_elements_by_class_name('divar-modal-footer')[0]
        agree_btn = div.find_element_by_class_name('button')
        agree_btn.click()
        time.sleep(2)
    # type text
    number_area = driver.find_element_by_class_name('post-fields-item__value')
    number = number_area.text
    try:
        number = int(number)
        data = {'number': number, "main-category": main_category,
                "category": category, "title": title}
    except:
        data = 0
    # driver.close()
    return data


# print(get_phone(link))
