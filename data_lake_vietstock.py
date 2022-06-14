from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import requests
import warnings
warnings.filterwarnings('ignore')
wd = webdriver.Chrome(executable_path='C:\webdrive\Driver\chromedriver.exe')
# wd = webdriver.ChromiumEdge(executable_path='C:\webdrive\Driver\msedgedriver.exe')
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



def login_vietstock(wd, ):
    wd.find_element_by_id('txtEmailLogin').send_keys('iyr60266@xcoxc.com')
    wd.find_element_by_id('txtPassword').send_keys('xuanphong2002')
    wd.find_element_by_id('btnLoginAccount').click()


def listing_new_vietstock(wd, id_page):
    wd.find_element_by_xpath('//*[@id="btn-page-next"]/i').click()
    soup = BeautifulSoup(wd.page_source, 'html.parser')
    table_source = soup.find_all('table', {'class':'table table-striped table-bordered table-hover table-middle pos-relative m-b'})
    table = pd.read_html(str(table_source))[0]
    list_href = []
    for tr in table_source[0].tbody:
        list_href.append(tr.find_all('a')[0]['href'])
    table['link'] = list_href
    return table

def listing_vietstock():
    url = 'https://finance.vietstock.vn/doanh-nghiep-a-z?page=1'
    wd.get(url)
    wd.maximize_window()
    # wd.find_element_by_xpath('/html/body/div[2]/div[6]/div/div[2]/div[2]/a[3]').click()
    # wd.find_element_by_class_name('title-link btnlogin').click()
    WebDriverWait(wd, 20).until(EC.visibility_of_all_elements_located((By.XPATH, "/html/body/div[2]/div[6]/div/div[2]/div[2]/a[3]")))[0].click()
    login_vietstock(wd)
    time.sleep(1)
    soup = BeautifulSoup(wd.page_source, 'html.parser')
    page_numbers = soup.find_all('span', {'class':'m-r-xs'})[0].find_all('span')[1].text
    table = listing_new_vietstock(wd, 1)
    for id_page in range(1, int(page_numbers)):
        time.sleep(0.2)
        table_new = listing_new_vietstock(wd, id_page)
        print(table_new)
        table = pd.concat([table, table_new])
    table.to_csv('Data_lake/save_vietstock.csv', index= False)

listing_vietstock()