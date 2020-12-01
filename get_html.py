# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from time import sleep
import pyautogui
from selenium.webdriver.common.action_chains import ActionChains
import time
import sys
from selenium.webdriver.common.keys import Keys
from PIL import Image

driver = webdriver.Chrome()
driver.maximize_window() # 窗口最大化
# driver = webdriver.Chrome()


# coin_list = ["bitcoin", "bitcoin-cash", "ethereum","litecoin", "xrp", "monacoin", "ethereum-classic"]

coin_list = ["bitcoin", "bitcoin-cash", "ethereum","litecoin", "xrp", "monacoin", "ethereum-classic","nem","lisk","bitcrystals","qash","counterparty","comsa-eth","horizen","tether", "binance-coin", "eos", "bitcoin-sv","dogecoin","stellar","cardano","qtum","factom"]


for i in coin_list:
        
    #first page -------------------------------------------------
    driver.get('https://coinmarketcap.com/currencies/'+ i + '/historical-data/?start=20201101&end=202001201')
    driver.implicitly_wait(2)
    print(driver.page_source)
    f = open('coin/'+i+'.html','w')
    f.write(str(driver.page_source))
    f.close()
    time.sleep(2)


try:
    
    driver.quit()
except:
    driver.quit()
    print("Unexpected error:", sys.exc_info()[0])
