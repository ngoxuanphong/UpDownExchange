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

wd.get