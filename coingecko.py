
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
rate = 107.677399
class MC():
    def __init__(self,coin):

        self.coin = coin

        self.table = data.add_sheet(coin)
        self.excel()

    def excel(self):

        self.table.write(0,1,u'open')
        self.table.write(0,2,u'close')
        

    def get_data(self):
        #start=20200101&end=20200202"
        url = "https://www.coingecko.com/en/coins/fisco/historical_data/usd?end_date=2020-10-02&start_date=2020-09-01#panel"
        print(url)
        headers = {'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Mobile Safari/537.36','Cookie': '_session_id=023925b7f9b6f85fdd910b0c0ffcbf29; path=/; expires=Sat, 03 Oct 2020 05:53:09 GMT; HttpOnly'}
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
        
        tr_list = bsObj.findAll('td', class_='text-center')
        j = 1
        k = 0
        print("===")
        print(len(date_str_list))
        print(len(tr_list))
        print("===")
        for index, i in enumerate(tr_list):
            text = i.text.replace(",","")
            text = text.replace("$","")
            if index % 3 == 0:
                j = j + 1
                print(index)
                self.table.write(j,0,str(date_str_list[int(index / 3) ]))
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
        coin_list =  ["caica-coin"]

        for i in coin_list:
            mc = MC(i)
            mc.get_data()
            file_name = time.strftime("%Y-%m-%d", time.localtime())
            time.sleep(3)
        data.save(file_name + '-coingecko.xls')

    except Exception as e:
        print(str(e))



# CICC https://www.coingecko.com/en/coins/caica-coin/historical_data/usd#panel
