from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

path_to_chromedriver = r"C:\Users\macie\OneDrive\DS z Maćkiem\Web Scraping\chromedriver.exe"
chrome_options = Options()
driver = webdriver.Chrome(executable_path=path_to_chromedriver, options=chrome_options)

driver.get("https://remit.orlen.pl/#/events/energy/all")

dataFrom = driver.find_element_by_id('dateFrom')
dataFrom.clear()
dataFrom.send_keys("01-01-2020")



dataFrom = driver.find_element_by_id('dateTo')
dataFrom.clear()
dataFrom.send_keys("31-01-2020")



### Wybier zdarzenia
typy_zdarzen = ['NIEPLANOWANE']
driver_typzdarzen = driver.find_elements_by_class_name("remit-checkbox")[0]
checkbox_list = driver_typzdarzen.find_elements_by_class_name('checkbox-img')
checkbox_name_list = driver_typzdarzen.find_elements_by_class_name("ng-binding")

if len(checkbox_list) == len(checkbox_name_list):
    for i, element in enumerate(checkbox_name_list):
        if element.text in typy_zdarzen:
            checkbox_list[i].click()

### Wybierz elektrownie
jednostki = ['CCGT Włocławek']
driver_typelektrowni = driver.find_elements_by_class_name("remit-checkbox")[1]
checkbox_list = driver_typelektrowni.find_elements_by_class_name('checkbox-img')
checkbox_name_list = driver_typelektrowni.find_elements_by_class_name("ng-binding")

if len(checkbox_list) == len(checkbox_name_list):
    for i, element in enumerate(checkbox_name_list):
        if element.text in jednostki:
            checkbox_list[i].click()

# search
driver.find_elements_by_tag_name("button")[0].click()

driver.find_elements_by_class_name("btn-save")[0].click()

from urllib import request

outfilename = "orlen_remit.xlsx"
url = r"https://remit.orlen.pl/xlsx/energy?dateFrom=2020/01/01&dateTo=2020/02/01"

request.urlretrieve(url, outfilename)