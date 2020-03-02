


import requests
from datetime import datetime
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
    # print(open_price," ",hight_price," ",low_price," ",close_price)
    # print("%.4f" % hight_price)
    print("%.2f" % open_price,"%.2f" % hight_price,"%.2f" % low_price,"%.2f" % close_price,"%.2f" % volume,str(d))
    if index == 27:
        break

