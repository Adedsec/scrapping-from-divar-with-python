from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time


# gets data from each agahi ! and returns a dictionary
def get_data(mydriver, link):
    # options = webdriver.ChromeOptions()
    # options.add_argument('--ignore-certificate-errors')
    # options.add_argument("--test-type")
    # options.binary_location = "C:/webdrivers/chromedriver.exe"
    driver = mydriver
    driver.get(link)

    data = {}

    attrs = {}

    title_field = driver.find_element_by_class_name('kt-page-title__title')
    title = title_field.text
    # print(title)

    data['title'] = title

    cat_field = driver.find_elements_by_class_name('kt-breadcrumbs__item')
    category = cat_field[len(cat_field)-2].text
    # print(category)

    data['category'] = category

    try:
        row_field = driver.find_elements_by_css_selector(
            'div.kt-group-row-item')

        meter = row_field[0].find_element_by_class_name(
            'kt-group-row-item__value').text

        year = row_field[1].find_element_by_class_name(
            'kt-group-row-item__value').text

        room = row_field[2].find_element_by_class_name(
            'kt-group-row-item__value').text

        attrs['متراژ'] = meter
        attrs['سال ساخت'] = year
        attrs['تعداد اتاق'] = room
    except:
        pass

    names = driver.find_elements_by_css_selector(
        '.kt-unexpandable-row__title')
    # print(len(names))
    attributes = driver.find_elements_by_css_selector(
        '.kt-unexpandable-row__value')
    # print(len(attributes))

    for i in range(len(attributes)):
        attrs[names[i+1].text] = attributes[i].text

    try:
        desc_field = driver.find_element_by_class_name(
            'kt-description-row__text')
        description = desc_field.text
        attrs['description'] = description
    except:
        pass

    data['attributes'] = attrs

    return data
