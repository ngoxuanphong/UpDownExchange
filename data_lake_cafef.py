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

def listing_cafe():
    url = "https://s.cafef.vn/du-lieu-doanh-nghiep.chn"
    wd.get(url)
    element = wd.find_elements_by_xpath('//*[@id="CafeF_ThiTruongNiemYet_Trang"]/a[2]')
    element[0].click()
    time.sleep(3)
    soup = BeautifulSoup(wd.page_source, 'html.parser')

    arr = soup.find_all("table")
    table = pd.read_html(str(arr))[4]
    Link = []
    count = 0
    for element in arr[4].find_all("a"):
        count += 1
        if count % 2 == 1:
            Link.append(element["href"])
    table["Link"] = Link
    table = table.rename(columns={"MÃ CK": "Symbol", "TÊN CÔNG TY": "Name Company", "SÀN": "Exchange"})
    table = table.drop(columns=["GIÁ"])
    table.to_csv('Data_lake/save_cafef.csv', index= False)
    # return table

listing_cafe()


def getExchange(s):
    try:
        t = s.split("/")[1]
    except:
        t = "NONE"
    return t


def getLink(s):
    try:
        t = s.split("/")[2]
    except:
        t = "NONE"
    return t


def getSymbol(s):
    try:
        t = s.split("/")[0]
    except:
        t = "NONE"
    return t

def getName(s):
    return s.split("/")[1]
    try:
        t = s.split("/")[0]
    except:
        t = "NONE"
    return t


# df["Exchange"] = df.apply(lambda row : getExchange(row["Link"]),axis=1)
# df["LinkCompany"] = df.apply(lambda row : getLink(row["Link"]),axis=1)
# df["Symbol"] = df.apply(lambda row : getSymbol(row["Symbol"]),axis=1)
# df["Name"] = df.apply(lambda row : getName(row["Symbol"]),axis=1)
# df = df.drop(columns=["Link"])
# df
