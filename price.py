from urllib.request import urlopen,Request
from bs4 import BeautifulSoup
import xlwt # write excel 新建一个Excel文件（只能通过新建写入）
import time
import math
from datetime import datetime

data = xlwt.Workbook()

style = xlwt.XFStyle()  # 创建一个样式对象，初始化样式

font = xlwt.Font() 
font.name = "Calibri" # ??'Times New Roman'
style.font = font

al = xlwt.Alignment()
al.horz = 0x01      
al.vert = 0x01      
style.alignment = al
# Calibri
rate = 107.37
class MC():
    def __init__(self,coin):

        self.coin = coin

        self.table = data.add_sheet(coin)
        self.excel()

    def excel(self):

        self.table.write(0,1,u'open')
        self.table.write(0,2,u'high')
        self.table.write(0,3,u'low')
        self.table.write(0,4,u'close')
        self.table.write(0,5,u'volume')
        self.table.write(0,6,u'marketcap')
        

    def get_data(self):
        #start=20200101&end=20200202"
        url = "https://coinmarketcap.com/currencies/" + self.coin +"/historical-data/?start=20200301&end=202000401"
        print(url)
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
        req = Request(url=url, headers=headers)
        html = urlopen(req).read()

        bsObj = BeautifulSoup(html,"html.parser")

        # 

        date_list = bsObj.findAll('td', class_='cmc-table__cell cmc-table__cell--sticky cmc-table__cell--left')
        date_str_list = []
        for i in date_list:
            d = i.text.replace(",","")
            datetime_object = datetime.strptime(d, '%b %d %Y')
            date_str_list.append(datetime_object)
            # print(str(datetime_object))
        
        tr_list = bsObj.findAll('td', class_='cmc-table__cell cmc-table__cell--right')
        j = 1
        k = 0
        print("===")
        print(len(date_str_list))
        print(len(tr_list))
        print("===")
        for index, i in enumerate(tr_list):
            text = i.text.replace(",","")
            if index % 6 == 0:
                print("---")
                j = j + 1
                print(index)
                self.table.write(j,0,str(date_str_list[int(index / 6) ]))
                k = 0
                
            # if k < 4 or k == 5:
            #     price = float(text) * rate
            #     price = "%.4f" % float(price) 
            #     self.table.write(j,k,price)
            # else:
            #     self.table.write(j,k,text)
            price = float(text) * rate
            price = "%.4f" % float(price) 
            price = price.replace(",","")
            self.table.write(j,k+1,price)
            
            k = k + 1
        
           

if __name__ == "__main__":
    
    try:
        # stellar xml
        # coin_list = ["bitcoin", "bitcoin-cash", "ethereum","litecoin", "xrp", "monacoin", "ethereum-classic"]
        coin_list = ["nem", "lisk", "bitcrystals", "comsa-eth", "factom", "pepe-cash", "qash", "storjcoin-x","counterparty"]
        coin_list = ["horizen","tether", "binance-coin", "eos", "bitcoin-sv","dogecoin","stellar","cardano","qtum"]

        for i in coin_list:
            mc = MC(i)
            mc.get_data()
            file_name = time.strftime("%Y-%m-%d", time.localtime())
            time.sleep(3)
        data.save(file_name + '.xls')

    except Exception as e:
        print(str(e))