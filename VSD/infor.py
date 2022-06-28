from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException  
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import requests
import pandas as pd

def get_niemyet_infor(link):
    res = requests.get(link)
    soup = BeautifulSoup(res.content, 'html.parser')
    table_source = soup.find_all('div', {'class':'news-issuers'})
    table = pd.read_html(str(table_source))[0]
    source_keys = [i.text for i in soup.find_all('div', {'class':'col-md-4 col-sm-6 item-info'})]
    source_values = [i.text for i in soup.find_all('div', {'class':'col-md-8 col-sm-6 item-info item-info-main'})]
    return table, pd.DataFrame({'Keys':source_keys, 'Values':source_values})

all_com = pd.read_csv('isin.csv')
for i in range(0, len(all_com.index)):
    symbol = all_com['Mã chứng khoán'].iloc[i]
    link = all_com['link_isin'].iloc[i]
    print(i, symbol, link)
    table1, table2 = get_niemyet_infor(link)
    table1.to_csv(f'data_lake/niemyetbs/{symbol}.csv', index = False)
    table2.to_csv(f'data_lake/infor/{symbol}.csv', index = False)
    table1.to_csv(f'/content/drive/MyDrive/Data Lake/Ingestion/Day 0/VSD/Volume/VolumeAdditionalEvents/{symbol}.csv', index = False)
    table2.to_csv(f'/content/drive/MyDrive/Data Lake/Ingestion/Day 0/VSD/Volume/VolumeNow/{symbol}.csv', index = False)