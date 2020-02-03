from urllib.request import urlopen,Request
from bs4 import BeautifulSoup
import xlwt # write excel 新建一个Excel文件（只能通过新建写入）
import time

class MC():
    def __init__(self,coin):

        self.coin = coin
        self.data = xlwt.Workbook()
        self.table = self.data.add_sheet('mfc')
        self.excel()

    def excel(self):
        self.table.write(0,0,u'date')
        self.table.write(0,1,u'open')
        self.table.write(0,2,u'high')
        self.table.write(0,3,u'low')
        self.table.write(0,4,u'close')
        self.table.write(0,5,u'volume')
        self.table.write(0,6,u'marketcap')
        

    def get_data(self):

        url = "https://coinmarketcap.com/currencies/bitcoin/historical-data/?start=20200104&end=20200203"
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
        req = Request(url=url, headers=headers)
        html = urlopen(req).read()

        bsObj = BeautifulSoup(html,"html.parser")
        tr_list = bsObj.findAll('td', class_='cmc-table__cell cmc-table__cell--right')
        j = 2
        k = 0
        for index, i in enumerate(tr_list):
            text = i.text.replace(",","")
            if index % 6 == 0:
                print("")
                j = j + 1
                k = 0

            self.table.write(j,k,text)
            k = k + 1
        file_name = time.strftime("%Y-%m-%d", time.localtime())
        self.data.save(file_name + '.xls')
           

if __name__ == "__main__":
     
    mc = MC("BTC")
    mc.get_data()
    # try:
            
    #     mc = MC("BTC")
    #     mc.get_data()
    # except Exception as e:
    #     print(str(e))