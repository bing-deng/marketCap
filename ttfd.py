


import requests
from datetime import datetime
import xlwt # write excel 新建一个Excel文件（只能通过新建写入）


data = xlwt.Workbook()
table = data.add_sheet("ttfd")
table.write(0,1,u'open')
table.write(0,2,u'high')
table.write(0,3,u'low')
table.write(0,4,u'close')
table.write(0,5,u'volume')
table.write(0,6,u'marketcap')

url = "https://openapi.ttf.one/open/api/get_records?symbol=ttfdusdt&period=1440"
r = requests.get(url).json()
l = r["data"]

for index,i in enumerate(l[::-1]):
    d =  datetime.fromtimestamp(i[0])
    # print(d,end=" ")
    rate = 107.677399
    open_price = i[1] * rate
    hight_price = i[2] * rate
    low_price = i[3] * rate
    close_price = i[4] * rate
    volume = i[5] * rate

    table.write(index + 1,0,str(d))
    table.write(index + 1,1,"%.2f" % open_price)
    table.write(index + 1,2,"%.2f" % hight_price)
    table.write(index + 1,3,"%.2f" % low_price)
    table.write(index + 1,4,"%.2f" % close_price)
    table.write(index + 1,5,"%.2f" % volume)

    # print(open_price," ",hight_price," ",low_price," ",close_price)
    # print("%.4f" % hight_price)
    print("%.2f" % open_price,"%.2f" % hight_price,"%.2f" % low_price,"%.2f" % close_price,"%.2f" % volume,str(d).replace(" 01:00:00",""))
    if index == 27:
        break


data.save("ttfd" + '-ttfd.xls')

