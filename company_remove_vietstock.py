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


symbol = 'AVS'
all_com = pd.read_csv('AllCompany.csv')
def nganh(symbol):
    link = f"htt  ps://finance.vietstock.vn/{symbol}-ctcp-chung-khoan-au-viet.htm"
    header = {'Accept': '/', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.158 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US;q=0.5,en;q=0.3', 'Cache-Control': 'max-age=0', 'Upgrade-Insecure-Requests': '1', 'Referer': 'https://google.com'}

    rs = requests.get(link,headers=header)
    soup = BeautifulSoup(rs.content, 'html.parser')
    try:
        table_source = soup.find_all('div', {'class':'m-b-xs sector-level'})[0]
        return table_source.text.upper()
    except:
        return np.nan
all_com['nganh'] = np.nan
for i in range(len(all_com.index)):
    symbol = all_com['Symbol'].iloc[i]
    print(symbol)
    all_com['nganh'].iloc[i] = nganh(symbol)
all_com.to_csv('AllCompanyVN.csv', index = False)
# print(all_com)