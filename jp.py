from urllib.request import urlopen,Request
from bs4 import BeautifulSoup
import xlwt # write excel 新建一个Excel文件（只能通过新建写入）
import time
import math
from datetime import datetime
# from fake_useragent import UserAgent #用于随机生成user-agent


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
rate = 103.071532

class MC():
    def __init__(self,coin):

        self.coin = coin

        self.table = data.add_sheet(coin)
        self.excel()

    def excel(self):

        self.table.write(0,1,u'公司名称')
        self.table.write(0,2,u'公司详细')
        self.table.write(0,3,u'low')
        self.table.write(0,4,u'close')
        self.table.write(0,5,u'volume')
        self.table.write(0,6,u'marketcap')
        

    def get_data(self):
        #start=20200101&end=20200202"04/28/2013

        url = "https://coinmarketcap.com/currencies/" + self.coin +"/historical-data/?start=20201101&end=202001201"
        # print(url)
        # ua = UserAgent()

        # headers = {'User-Agent':ua.random}
        # req = Request(url=url, headers=headers)
        # html = urlopen(req).read()
        # time.sleep(4)
        # print(html)
        # bsObj = BeautifulSoup(html,"html.parser")
        bsObj = BeautifulSoup(open('./coin/' + self.coin+'.html').read())

        # 
        date_list = bsObj.findAll('td', class_='')
        print("=-=-=-=-=-=-=-",date_list)
        row = 1
        k = 0
        for i in date_list:

            i = i.text
            if '$' not in i:
                i = i.replace(",","")
                i = str(datetime.strptime(i, '%b %d %Y')).replace(" 00:00:00","")
                print("日期",str(i))
                row = row + 1
                k = 0
            else:
                i = i.replace("$","").replace(",","")
                i = float(i) * rate
                i = "%.4f" % float(i) 
            self.table.write(row,k,i)
            k = k + 1
        
        # date_str_list = []
        # for i in date_list:
        #     d = i.text.replace(",","")
        #     if "$" not in d:
        #         datetime_object = datetime.strptime(d, '%b %d %Y')
        #         date_str_list.append(datetime_object)
        #         print("datetime_object",str(datetime_object))
        
        # tr_list = bsObj.findAll('td', class_='')
        # j = 1
        # k = 0
        # print("===")
        # print(len(date_str_list),type(date_list),len(date_list))
        # print(len(tr_list))
        # print("===")
        # for index, i in enumerate(tr_list):
        #     text = i.text.replace(",","")
        #     if index % 6 == 0:
        #         print("---")
        #         j = j + 1
        #         print('price',index,i)
        #         self.table.write(j,0,str(date_str_list[int(index / 6) ]))
        #         k = 0
                
        #     # if k < 4 or k == 5:
        #     #     price = float(text) * rate
        #     #     price = "%.4f" % float(price) 
        #     #     self.table.write(j,k,price)
        #     # else:
        #     #     self.table.write(j,k,text)
        #     if '$' in i:
        #         price = float(text) * rate
        #         price = "%.4f" % float(price) 
        #         price = price.replace(",","")
        #         self.table.write(j,k+1,price)
                
        #         k = k + 1
        
        

if __name__ == "__main__":
    
    try:
        # stellar xml
        coin_list = ["bitcoin", "bitcoin-cash", "ethereum","litecoin", "xrp", "monacoin", "ethereum-classic","nem","lisk","bitcrystals","qash","counterparty","comsa-eth","horizen","tether", "binance-coin", "eos", "bitcoin-sv","dogecoin","stellar","cardano","qtum","factom"]
        coin_list = ["bitcoin", "bitcoin-cash", "ethereum","litecoin", "xrp", "monacoin"]
        coin_list = ["ethereum-classic","nem","lisk","bitcrystals","qash","counterparty"]
        coin_list = ["comsa-eth","horizen","tether", "binance-coin", "eos", "bitcoin-sv","dogecoin","stellar","cardano","qtum","factom"]
        # coin_list = ["nem","lisk","bitcrystals","qash","counterparty","comsa-eth"]
        # coin_list = ["horizen","tether", "binance-coin", "eos", "bitcoin-sv","dogecoin","stellar","cardano","qtum","factom"]
        # coin_list = ["bitcoin"]
        
        for i in coin_list:
            mc = MC(i)
            mc.get_data()
            file_name = time.strftime("%Y-%m-%d", time.localtime())
            time.sleep(5)
        data.save(file_name + '.xls')

    except Exception as e:
        print(str(e))