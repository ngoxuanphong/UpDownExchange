from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import requests
import warnings
warnings.filterwarnings('ignore')
wd = webdriver.ChromiumEdge(executable_path='C:\webdrive\Driver\msedgedriver.exe')

# def listing_cophieu68():

# res = requests.get('https://www.cophieu68.vn/companylist.php?currentPage=1&o=s&ud=a', verify = False)
url = 'https://www.cophieu68.vn/companylist.php?currentPage=1&o=s&ud=a'
wd.get(url)
soup = BeautifulSoup(wd.page_source, 'html.parser')
table_source = soup.find_all("table")
for i in table_source:
    print(i)