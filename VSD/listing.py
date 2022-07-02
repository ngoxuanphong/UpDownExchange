from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException  
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import requests

import warnings 
warnings.filterwarnings('ignore')
# wd = webdriver.ChromiumEdge(executable_path='C:\webdrive\Driver\msedgedriver.exe')
wd = webdriver.Chrome(executable_path='C:\webdrive\Driver\chromedriver.exe')
def click_to_data(wd, id):
    try:
        element = wd.find_element_by_id(f'{id}')
        element.click()
    except:
        pass

# divListMaCKChuyenSan

def getTable(wd):
    sort_link = 'https://www.vsd.vn/vi'
    source_page = BeautifulSoup(wd.page_source,'html.parser')
    # table = source_page.find_all("table", {'id':'tblListMaISIN'})
    table = source_page.find_all("table", {'id':'tblListMaCKChuyenSan'})
    print(table)
    table_isin = pd.read_html(str(table))[0]
    print(table_isin)
    # link_isin = []
    # link_td = []
    # for tr in source_page.find_all('tr'):
    #     list_td =  tr.find_all('td')
    #     if len(list_td) == 4:
    #         link_isin.append(sort_link+list_td[1].find_all('a')[0]['href'])
    #         link_td.append(sort_link + list_td[3].find_all('a')[0]['href'])
    table_isin = pd.read_html(str(table))[0]
    # table_isin['link_isin'] = link_isin
    # table_isin['link_td'] = link_td
    return table_isin

def getlink():
    # url = 'https://www.vsd.vn/vi/tra-cuu-thong-ke/TK_MACK_HUYDK?tab=3'
    url = 'https://www.vsd.vn/vi/tra-cuu-thong-ke/TK_MACK_HUYDK?tab=4'
    wd.get(url)
    wd.maximize_window()
    
getlink()
table_isin = getTable(wd)
for id_page in range(2, 71):
    time.sleep(2)
    click_to_data(wd, id_page)
    time.sleep(2)
    table_new = getTable(wd)
    table_isin = pd.concat([table_isin, table_new])
print(table_isin)
table_isin.to_csv('infor_change_exchange.csv', index = False)