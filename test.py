from msilib.schema import tables
from turtle import window_height
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

''' 
    publishStartDate = ""
    publishEndDate = ""
    dataCount = 0
    expiryDate = "" 
'''

driver = webdriver.Chrome('C:\\Users\GoodTenders\Desktop\chromeD\chromedriver.exe')

driver.get('https://www.globaltenders.com/')
time.sleep(5)

tables = '/html/body/div[6]/div/div[2]/div/div/table[1]/tbody/tr/td/table/tbody/tr[5]/td/table/tbody/tr/td/a[1]'

fatching_table = driver.find_element_by_xpath(tables).click()

#data = "table > tbody > tr:nth-child(5) > td"

#data = '.tbsum > tr:nth-child(9) > td'

data = '.tbsum > tr:nth-child(9)'

time.sleep(5)

submit = driver.find_element_by_css_selector(data).text

print(submit)

with open(submit) as file_in:
    lines = []
    for line in file_in:
        lines.append(line.strip('\n'))
    print(lines)
