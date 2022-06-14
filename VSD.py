from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException  
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import requests

import warnings 
warnings.filterwarnings('ignore')
from selenium.webdriver.common.keys import Keys
wd = webdriver.ChromiumEdge(executable_path='C:\webdrive\Driver\msedgedriver.exe')
# wd = webdriver.Chrome(executable_path='C:\webdrive\chromedriver.exe')
def click_to_data(wd, id):
    try:
        wd.find_element_by_id(f'{id}').click()
    except:
        pass
    soure_page = BeautifulSoup(wd.page_source,'html.parser')
    table = soure_page.find_all("table", {'id':'tblListMaISIN'})
    table_isin = pd.read_html(str(table))[0]
    return table_isin

def table_isin():
    url = 'https://www.vsd.vn/vi/tra-cuu-thong-ke/TK_MACK_HUYDK?tab=3'
    wd.get(url)
    source_page = BeautifulSoup(wd.page_source,'html.parser')
    table = source_page.find_all("table", {'id':'tblListMaISIN'})
    table_isin = pd.read_html(str(table))[0]
    for i in range(2, 452):
        time.sleep(1)
        table_new = click_to_data(wd, i)
        table_isin = pd.concat([table_isin, table_new])
    table_isin.to_csv('Data_lake/save_VSD.csv', index = False)

def click_to_data_delisting(wd, id):
    html = wd.find_element_by_tag_name('html')
    # table_hny = False
    # html.send_keys(Keys.PAGE_UP)
    wd.find_element_by_id(f'{id}').click()
    # except: 
    #     html.send_keys(Keys.PAGE_DOWN)
    # wd.find_element_by_id(f'{id}').click()
    # print(id)
    wd.execute_script("window.scrollTo(0, 700)")
    time.sleep(1)
    # print('hiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii')
    soure_page = BeautifulSoup(wd.page_source,'html.parser')
    table = soure_page.find_all("table", {'id':'tblListMaCKHuyDK'})
    table_hny = pd.read_html(str(table))[0]
    return table_hny

def table_delisting(wd):
    url = 'https://www.vsd.vn/vi/tra-cuu-thong-ke/TK_MACK_HUYDK?tab=5&fbclid=IwAR1fCyHCql21IClVIKfHrxV3JBjxqNwWOBz_AG8-KWdc4QRGxpUX6y9csPw'
    wd.get(url)
    wd.maximize_window()
    soure_page = BeautifulSoup(wd.page_source,'html.parser')
    table = soure_page.find_all("table", {'id':'tblListMaCKHuyDK'})
    table_hny1 = pd.read_html(str(table))[0]
    for i in range(2, 217):
        time.sleep(0.3)
        data_new = click_to_data_delisting(wd, i)
        # print(data_new)
        table_hny1 = pd.concat([table_hny1, data_new])
    table_hny1.to_csv('Data_lake/VSD_HuyNiemYet.csv', index = False)

def try_to_die():
    try:
        wd = webdriver.ChromiumEdge(executable_path='C:\webdrive\Driver\msedgedriver.exe')
        table_delisting(wd)
    except:
        wd.close()
        try_to_die()
try_to_die()

# table_delisting(wd)