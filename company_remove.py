from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import requests
from selenium.webdriver.support.ui import Select
import warnings
warnings.filterwarnings('ignore')
driver = webdriver.Chrome(executable_path='C:\webdrive\Driver\chromedriver.exe')

# wd = webdriver.ChromiumEdge(executable_path='C:\webdrive\Driver\msedgedriver.exe')

driver.get('https://s.cafef.vn/du-lieu-doanh-nghiep.chn?fbclid=IwAR0-qgHvkS2U89U2Da-gNfrVWesi1rTX13PbjxRSpfI9WzfvLF8ufLO7DzQ')
select = Select(driver.find_element_by_id('CafeF_ThiTruongNiemYet_Nganh'))
select.select_by_value('341')
driver.find_element_by_xpath('/html/body/form/div[3]/div/div[2]/div[2]/div[1]/div[4]/h1/div/div/div[1]/table/tbody/tr[3]/td/table/tbody/tr[2]/td[3]/img').click()
time.sleep(5)
driver.find_element_by_xpath('/html/body/form/div[3]/div/div[2]/div[2]/div[1]/div[4]/h1/div/div/div[1]/table/tbody/tr[6]/td/table/tbody/tr/td[2]/a[2]').click()
time.sleep(3)
soup = BeautifulSoup(driver.page_source, 'html.parser')

arr = soup.find_all("table")
table = pd.read_html(str(arr))[4]
table = table.rename(columns={"MÃ CK": "Symbol", "TÊN CÔNG TY": "Name Company", "SÀN": "Exchange"})
table = table.drop(columns=["GIÁ"])
table.to_csv('Data_lake/save_remove_cafef.csv', index= False)