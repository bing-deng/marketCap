import requests
from urllib.request import urlopen,Request
import json
from datetime import datetime
import xlwt

data = xlwt.Workbook()



class Btcbox():
    
    def __init__(self,coin):
        # lower 
        self.coin = coin
        self.table = data.add_sheet(coin)
        self.table.write(0,1,u'open')
        self.table.write(0,2,u'close')
        self.table.write(0,3,u'high')
        self.table.write(0,4,u'low')
        self.table.write(0,5,u'volume')

    def data(self):

        # https://www.unixtimestamp.com/
        #  https://www.btcbox.co.jp/index/tradingview/kline/coin/eth/type/history?symbol=AAPL&resolution=D&from=1601510400&to=1604102400

        # url = "https://www.btcbox.co.jp/index/tradingview/kline/coin/" +self.coin + "/type/history?symbol=AAPL&resolution=D&from=1552178781&to=1583282841"
        # # r = requests.get(url).json()
        # headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
        # req = Request(url=url, headers=headers)
        # html = urlopen(req).read()
        # print(html)

        eth = '{"t":[1601305200,1601391600,1601478000,1601564400,1601650800,1601737200,1601823600,1601910000,1601996400,1602082800,1602169200,1602255600,1602342000,1602428400,1602514800,1602601200,1602687600,1602774000,1602860400,1602946800,1603033200,1603119600,1603206000,1603292400,1603378800,1603465200,1603551600,1603638000,1603724400,1603810800,1603897200,1603983600,1604070000,1604156400,1604242800,1604329200,1604415600,1604502000,1604588400,1604674800,1604761200,1604847600,1604934000,1605020400,1605106800,1605193200,1605279600,1605366000,1605452400,1605538800,1605625200,1605711600,1605798000,1605884400,1605970800,1606057200,1606143600,1606230000,1606316400,1606402800,1606489200,1606575600,1606662000,1606748400],"c":["37763.00000000","37596.00000000","38557.00000000","36425.00000000","36619.00000000","36711.00000000","37311.00000000","36514.00000000","36194.00000000","37010.00000000","38100.00000000","39398.00000000","39353.00000000","40295.00000000","40087.00000000","40002.00000000","39605.00000000","38666.00000000","38841.00000000","39579.00000000","40070.00000000","39060.00000000","40412.00000000","43294.00000000","43440.00000000","43461.00000000","42800.00000000","42418.00000000","42118.00000000","40333.00000000","40852.00000000","39608.00000000","40718.00000000","40630.00000000","40410.00000000","40304.00000000","39924.00000000","42920.00000000","45644.00000000","46128.00000000","46850.00000000","46606.00000000","46802.00000000","48677.00000000","48430.00000000","49455.00000000","48290.00000000","48003.00000000","48046.00000000","48945.00000000","48982.00000000","49559.00000000","52300.00000000","55302.00000000","55034.00000000","62081.00000000","60462.00000000","61650.00000000","52399.00000000","52810.00000000","54803.00000000","57577.00000000","62705.00000000","62692.0000000000"],"o":["38377","37770","37643","38557","36463","36619","36714","37321","36476","36212","37032","38095","39419","39394","40362","40091","40000","39641","38683","38854","39585","40058","39040","40443","43351","43328","43457","42832","42405","42113","40333","40862","39621","40643","40611","40430","40309","39937","43045","45653","46315","47000","46602","46829","48694","48430","49544","48293","48000","48060","48893","48954","49600","52300","55307","55035","62034","59355","61708","52279","52884","54818","57561","62689.0000000000"],"h":["38837.00000000","38098.00000000","38909.00000000","38603.00000000","36900.00000000","37065.00000000","37521.00000000","37540.00000000","37271.00000000","37041.00000000","38400.00000000","39919.00000000","39833.00000000","40511.00000000","41496.00000000","40734.00000000","40143.00000000","40154.00000000","38957.00000000","39776.00000000","40192.00000000","40495.00000000","40500.00000000","43475.00000000","44000.00000000","43569.00000000","43698.00000000","43128.00000000","42506.00000000","42766.00000000","41063.00000000","41220.00000000","41211.00000000","40901.00000000","42345.00000000","40821.00000000","40879.00000000","42921.00000000","46067.00000000","48371.00000000","47026.00000000","47737.00000000","47712.00000000","48799.00000000","50155.00000000","49633.00000000","49938.00000000","48633.00000000","48227.00000000","49144.00000000","51486.00000000","49959.00000000","52928.00000000","55592.00000000","58201.00000000","62592.00000000","64500.00000000","62695.00000000","61850.00000000","55328.00000000","55007.00000000","58160.00000000","63000.00000000","63999.0000000000"],"l":["36449.00000000","37250.00000000","37497.00000000","35265.00000000","36063.00000000","36314.00000000","36542.00000000","36400.00000000","35288.00000000","35580.00000000","36788.00000000","38008.00000000","38955.00000000","38643.00000000","39655.00000000","39718.00000000","39045.00000000","38167.00000000","38336.00000000","38548.00000000","39328.00000000","38780.00000000","38787.00000000","40255.00000000","42783.00000000","42212.00000000","42428.00000000","42190.00000000","40243.00000000","39800.00000000","39804.00000000","39109.00000000","39621.00000000","40219.00000000","39611.00000000","38966.00000000","39626.00000000","39916.00000000","42335.00000000","41600.00000000","44197.00000000","45792.00000000","45935.00000000","46468.00000000","47852.00000000","47676.00000000","47551.00000000","47500.00000000","46204.00000000","47790.00000000","47990.00000000","48221.00000000","48769.00000000","51744.00000000","53101.00000000","54927.00000000","58582.00000000","56804.00000000","50390.00000000","50407.00000000","51439.00000000","54652.00000000","57261.00000000","62001.0000000000"],"v":["1146.83360000","830.33900000","819.87160000","865.95630000","359.96850000","316.52070000","575.34060000","582.13270000","687.88020000","842.13070000","982.16830000","970.07100000","864.38730000","931.09070000","862.66040000","847.17000000","852.84060000","846.09380000","858.28080000","849.34180000","798.24420000","664.96390000","710.13940000","741.79130000","679.86740000","663.35740000","682.03000000","666.24030000","720.77560000","678.41370000","707.09900000","690.15240000","680.66020000","654.11700000","732.74120000","682.16360000","668.10320000","715.20610000","729.81560000","478.86250000","282.13360000","328.81480000","389.94890000","335.71170000","312.11930000","327.79610000","330.61540000","296.17910000","475.42880000","978.04280000","892.93360000","776.27320000","1001.95520000","847.78640000","817.25370000","980.29880000","790.00640000","352.71840000","562.27250000","990.02550000","847.12180000","948.20350000","977.40270000","371.11570000"],"s":"ok"}'

        btc = '{"t":[1601305200,1601391600,1601478000,1601564400,1601650800,1601737200,1601823600,1601910000,1601996400,1602082800,1602169200,1602255600,1602342000,1602428400,1602514800,1602601200,1602687600,1602774000,1602860400,1602946800,1603033200,1603119600,1603206000,1603292400,1603378800,1603465200,1603551600,1603638000,1603724400,1603810800,1603897200,1603983600,1604070000,1604156400,1604242800,1604329200,1604415600,1604502000,1604588400,1604674800,1604761200,1604847600,1604934000,1605020400,1605106800,1605193200,1605279600,1605366000,1605452400,1605538800,1605625200,1605711600,1605798000,1605884400,1605970800,1606057200,1606143600,1606230000,1606316400,1606402800,1606489200,1606575600,1606662000,1606748400],"c":["1139067.00000000","1137587.00000000","1146705.00000000","1112754.00000000","1111567.00000000","1119050.00000000","1134495.00000000","1129536.00000000","1128151.00000000","1156010.00000000","1169106.00000000","1198306.00000000","1200391.00000000","1208539.00000000","1203690.00000000","1196567.00000000","1200009.00000000","1193819.00000000","1198401.00000000","1205953.00000000","1229334.00000000","1258513.00000000","1323226.00000000","1353976.00000000","1357820.00000000","1366635.00000000","1361202.00000000","1383971.00000000","1396508.00000000","1363732.00000000","1403147.00000000","1399871.00000000","1444969.00000000","1444000.00000000","1414000.00000000","1440000.00000000","1448009.00000000","1545689.00000000","1603264.00000000","1582694.00000000","1585000.00000000","1589000.00000000","1604735.00000000","1648146.00000000","1680000.00000000","1701807.00000000","1677712.00000000","1680993.00000000","1713726.00000000","1783014.00000000","1841512.00000000","1884083.00000000","1925990.00000000","1946216.00000000","1891659.00000000","1920414.00000000","1913274.00000000","1988324.00000000","1751111.00000000","1747550.00000000","1804971.00000000","1878275.00000000","2019911.00000000","2026240.0000000000"],"o":["1148811","1139067","1137568","1146713","1111803","1111585","1119029","1134495","1129536","1128130","1156010","1169106","1198306","1200236","1208548","1204061","1196567","1199988","1193830","1198401","1205953","1229133","1258492","1323221","1353976","1355853","1366645","1361212","1383971","1398700","1363713","1403147","1399873","1442520","1443646","1414028","1443680","1447788","1545713","1603264","1582910","1585100","1588290","1602518","1648146","1680000","1701165","1677730","1680993","1713729","1783838","1841511","1884083","1926271","1946217","1891054","1913394","1925800","1988298","1750000","1744868","1804635","1878476","2020330.0000000000"],"h":["1153567.00000000","1148810.00000000","1151937.00000000","1149247.00000000","1116668.00000000","1121566.00000000","1137797.00000000","1142010.00000000","1136985.00000000","1156747.00000000","1175950.00000000","1209760.00000000","1204050.00000000","1213748.00000000","1233698.00000000","1213562.00000000","1203831.00000000","1220368.00000000","1200515.00000000","1211005.00000000","1229922.00000000","1260011.00000000","1323997.00000000","1379564.00000000","1380000.00000000","1370695.00000000","1393999.00000000","1388285.00000000","1408834.00000000","1444989.00000000","1408519.00000000","1427297.00000000","1465999.00000000","1454393.00000000","1449929.00000000","1440000.00000000","1470753.00000000","1551851.00000000","1655989.00000000","1626956.00000000","1595384.00000000","1641000.00000000","1630000.00000000","1654194.00000000","1698660.00000000","1726989.00000000","1712945.00000000","1692910.00000000","1719998.00000000","1784990.00000000","1920989.00000000","1886768.00000000","1925990.00000000","1971173.00000000","1963619.00000000","1930000.00000000","1926900.00000000","1998925.00000000","1994223.00000000","1819797.00000000","1810613.00000000","1897722.00000000","2052990.00000000","2052918.0000000000"],"l":["1125925.00000000","1127000.00000000","1129236.00000000","1095000.00000000","1104851.00000000","1110759.00000000","1117636.00000000","1127708.00000000","1113462.00000000","1119307.00000000","1120000.00000000","1163991.00000000","1190220.00000000","1185001.00000000","1195875.00000000","1195012.00000000","1188000.00000000","1181967.00000000","1189991.00000000","1192998.00000000","1202621.00000000","1227009.00000000","1252173.00000000","1314888.00000000","1343452.00000000","1334000.00000000","1352496.00000000","1356000.00000000","1342766.00000000","1348650.00000000","1355006.00000000","1372671.00000000","1399855.00000000","1428011.00000000","1386085.00000000","1394426.00000000","1422000.00000000","1446058.00000000","1537980.00000000","1572508.00000000","1486175.00000000","1569933.00000000","1568000.00000000","1590974.00000000","1635862.00000000","1671183.00000000","1652350.00000000","1650685.00000000","1655481.00000000","1708878.00000000","1776663.00000000","1796394.00000000","1839990.00000000","1911000.00000000","1831337.00000000","1866501.00000000","1870379.00000000","1909001.00000000","1720000.00000000","1702040.00000000","1713248.00000000","1804635.00000000","1871319.00000000","1980495.0000000000"],"v":["1735.00740000","1654.77600000","1538.12220000","973.37490000","450.59580000","1017.21240000","946.82280000","802.03090000","1374.24990000","1308.86390000","1290.41990000","1283.91600000","1389.66340000","909.99460000","923.76940000","1191.37030000","1215.59480000","1302.56340000","1391.03880000","1388.75650000","956.87330000","746.84710000","869.36040000","1041.92830000","1300.51760000","677.62540000","963.68780000","872.14840000","617.28740000","111.25090000","1498.98580000","1040.34100000","547.82733405","1487.43330000","764.61340000","1294.23040000","962.24250000","979.71160000","1164.06840000","1022.08280000","1020.04560000","1158.05740000","1327.24550000","1756.84910000","1239.70700000","755.29530000","1704.26670000","669.22140000","1240.97210000","936.07400000","611.40300850","570.67730000","937.43980000","1033.38350000","1850.33170000","1646.48010000","684.70880000","1139.36460000","785.48280000","1390.37650000","1588.24140000","1581.34720000","873.65220000","410.17360000"],"s":"ok"}'

        ltc = '{"t":[1601305200,1601391600,1601478000,1601564400,1601650800,1601737200,1601823600,1601910000,1601996400,1602082800,1602169200,1602255600,1602342000,1602428400,1602514800,1602601200,1602687600,1602774000,1602860400,1602946800,1603033200,1603119600,1603206000,1603292400,1603378800,1603465200,1603551600,1603638000,1603724400,1603810800,1603897200,1603983600,1604070000,1604156400,1604242800,1604329200,1604415600,1604502000,1604588400,1604674800,1604761200,1604847600,1604934000,1605020400,1605106800,1605193200,1605279600,1605366000,1605452400,1605538800,1605625200,1605711600,1605798000,1605884400,1605970800,1606057200,1606143600,1606230000,1606316400,1606402800,1606489200,1606575600,1606662000,1606748400],"c":["4821.00000000","4874.00000000","5115.00000000","4759.00000000","4795.00000000","4874.00000000","4920.00000000","4861.00000000","4886.00000000","4984.00000000","5063.00000000","5252.00000000","5261.00000000","5330.00000000","5221.00000000","5268.00000000","5234.00000000","4970.00000000","4987.00000000","5027.00000000","5045.00000000","4974.00000000","5386.00000000","5750.00000000","5770.00000000","6149.00000000","6269.00000000","6040.00000000","6024.00000000","5877.00000000","5824.00000000","5573.00000000","5823.00000000","5732.00000000","5683.00000000","5618.00000000","5466.00000000","6069.00000000","6343.00000000","6263.00000000","6325.00000000","6200.00000000","6119.00000000","6249.00000000","6157.00000000","6869.00000000","6644.00000000","6613.00000000","7372.00000000","7584.00000000","7416.00000000","8290.00000000","8535.00000000","8996.00000000","8524.00000000","9325.00000000","8850.00000000","9098.00000000","7738.00000000","7508.00000000","7480.00000000","7835.00000000","8652.00000000","8962.0000000000"],"o":["4913","4820","4877","5095","4729","4824","4846","4914","4861","4886","4984","5064","5226","5324","5330","5262","5266","5236","4968","4962","5028","5046","4952","5413","5750","5770","6160","6267","6035","6021","5873","5823","5576","5823","5732","5685","5620","5446","6076","6364","6259","6325","6202","6073","6234","6138","6868","6644","6612","7375","7540","7360","8357","8509","8995","8521","9264","8846","9149","7720","7506","7480","7800","8688.0000000000"],"h":["4961.00000000","4905.00000000","5131.00000000","5134.00000000","4828.00000000","4903.00000000","4971.00000000","4946.00000000","5108.00000000","4992.00000000","5075.00000000","5296.00000000","5377.00000000","5399.00000000","5400.00000000","5370.00000000","5299.00000000","5278.00000000","5059.00000000","5069.00000000","5069.00000000","5090.00000000","5480.00000000","5910.00000000","5936.00000000","6221.00000000","6285.00000000","6299.00000000","6128.00000000","6315.00000000","5920.00000000","5900.00000000","5899.00000000","5888.00000000","5954.00000000","5724.00000000","5700.00000000","6077.00000000","6554.00000000","6692.00000000","6380.00000000","6380.00000000","6272.00000000","6297.00000000","6344.00000000","6980.00000000","6947.00000000","6780.00000000","7552.00000000","7900.00000000","7993.00000000","8383.00000000","8739.00000000","9063.00000000","9243.00000000","9426.00000000","9629.00000000","9349.00000000","9166.00000000","7876.00000000","7735.00000000","8150.00000000","8831.00000000","9189.0000000000"],"l":["4753.00000000","4752.00000000","4816.00000000","4651.00000000","4680.00000000","4771.00000000","4829.00000000","4826.00000000","4775.00000000","4831.00000000","4932.00000000","5010.00000000","5109.00000000","5210.00000000","5142.00000000","5210.00000000","5170.00000000","4856.00000000","4903.00000000","4910.00000000","4938.00000000","4916.00000000","4910.00000000","5401.00000000","5545.00000000","5645.00000000","5940.00000000","6009.00000000","5801.00000000","5767.00000000","5575.00000000","5493.00000000","5575.00000000","5676.00000000","5577.00000000","5417.00000000","5424.00000000","5446.00000000","5975.00000000","6206.00000000","5976.00000000","6145.00000000","6071.00000000","6051.00000000","6102.00000000","6101.00000000","6520.00000000","6502.00000000","6410.00000000","7353.00000000","7259.00000000","7201.00000000","8213.00000000","8390.00000000","8139.00000000","8403.00000000","8700.00000000","8801.00000000","7653.00000000","7102.00000000","7260.00000000","7451.00000000","7759.00000000","8604.0000000000"],"v":["1024.22220000","1012.91950000","1067.79800000","1052.19690000","964.73600000","940.94550000","1075.44380000","1070.62190000","1129.40380000","1027.87720000","1061.75990000","1040.18750000","1155.68440000","1090.71140000","1065.32310000","1062.24760000","1069.56720000","1060.90730000","1023.01400000","1033.14410000","1040.84650000","998.74120000","1158.76910000","1144.82550000","1087.06730000","1042.06560000","1061.82360000","1002.00470000","952.99290000","1099.71990000","996.12260000","1072.49330000","1032.86190000","1043.70520000","936.92110000","1018.95220000","1078.75560000","1161.62050000","543.13570000","306.06580000","326.64000000","1360.11970000","2100.17840000","2068.33950000","2085.46130000","2051.64150000","1357.54980000","1149.01000000","1156.91410000","1146.67040000","1276.18000000","1249.19810000","1361.27850000","1186.81900000","1294.20710000","1393.81350000","1459.37530000","1125.19940000","1551.69170000","1100.55250000","1087.68960000","1136.78100000","1244.84640000","560.48460000"],"s":"ok"}'
        bch = '{"t":[1601305200,1601391600,1601478000,1601564400,1601650800,1601737200,1601823600,1601910000,1601996400,1602082800,1602169200,1602255600,1602342000,1602428400,1602514800,1602601200,1602687600,1602774000,1602860400,1602946800,1603033200,1603119600,1603206000,1603292400,1603378800,1603465200,1603551600,1603638000,1603724400,1603810800,1603897200,1603983600,1604070000,1604156400,1604242800,1604329200,1604415600,1604502000,1604588400,1604674800,1604761200,1604847600,1604934000,1605020400,1605106800,1605193200,1605279600,1605366000,1605452400,1605538800,1605625200,1605711600,1605798000,1605884400,1605970800,1606057200,1606143600,1606230000,1606316400,1606402800,1606489200,1606575600,1606662000,1606748400],"c":["24087.00000000","24028.00000000","24324.00000000","23210.00000000","23153.00000000","23191.00000000","23384.00000000","23096.00000000","23298.00000000","24736.00000000","25080.00000000","25440.00000000","25369.00000000","25261.00000000","26885.00000000","26520.00000000","27580.00000000","26573.00000000","26143.00000000","26178.00000000","26268.00000000","25763.00000000","26912.00000000","28406.00000000","28121.00000000","28949.00000000","28487.00000000","27816.00000000","27694.00000000","28326.00000000","27812.00000000","26957.00000000","27553.00000000","27369.00000000","27119.00000000","25525.00000000","24463.00000000","25857.00000000","26252.00000000","26675.00000000","28341.00000000","27646.00000000","27077.00000000","27300.00000000","27057.00000000","26810.00000000","26810.00000000","25595.00000000","26618.00000000","26583.00000000","25538.00000000","25933.00000000","26582.00000000","30012.00000000","29009.00000000","31222.00000000","33334.00000000","34879.00000000","27810.00000000","27445.00000000","28691.00000000","29153.00000000","30887.00000000","32409.0000000000"],"o":["24364","24066","24062","24374","23210","23179","23197","23385","23089","23298","24736","25071","25440","25344","25269","26757","26520","27618","26592","26114","26178","26256","25765","26934","28445","28066","28800","28489","27811","27711","28347","27831","26957","27574","27369","27132","25486","24476","25857","26417","26676","28349","27607","27077","27281","27078","26618","26810","25596","26618","26573","25527","25933","26582","29961","28914","31241","33333","34884","27811","27430","28701","29154","31127.0000000000"],"h":["24750.00000000","24438.00000000","24600.00000000","24510.00000000","23380.00000000","23380.00000000","23400.00000000","23571.00000000","24276.00000000","24800.00000000","25300.00000000","25955.00000000","25691.00000000","25590.00000000","26889.00000000","27270.00000000","27980.00000000","28090.00000000","26610.00000000","26401.00000000","26528.00000000","26504.00000000","27000.00000000","28622.00000000","28809.00000000","29110.00000000","29055.00000000","28670.00000000","28079.00000000","29199.00000000","28797.00000000","28286.00000000","27810.00000000","27645.00000000","28200.00000000","27300.00000000","25824.00000000","25941.00000000","26599.00000000","28651.00000000","28499.00000000","28498.00000000","28083.00000000","27510.00000000","27779.00000000","27300.00000000","27359.00000000","27159.00000000","27000.00000000","26810.00000000","26810.00000000","25977.00000000","26900.00000000","30339.00000000","32472.00000000","31673.00000000","38815.00000000","38211.00000000","35567.00000000","29410.00000000","28691.00000000","30373.00000000","31690.00000000","33494.0000000000"],"l":["23719.00000000","23793.00000000","23908.00000000","22509.00000000","22797.00000000","22901.00000000","22571.00000000","23026.00000000","22900.00000000","23265.00000000","24500.00000000","24805.00000000","25000.00000000","24500.00000000","25000.00000000","26303.00000000","26334.00000000","25783.00000000","25665.00000000","25493.00000000","25867.00000000","25297.00000000","25140.00000000","26725.00000000","27333.00000000","27698.00000000","28055.00000000","27805.00000000","26639.00000000","27024.00000000","26891.00000000","26840.00000000","26957.00000000","27108.00000000","26800.00000000","24831.00000000","24106.00000000","24013.00000000","25289.00000000","26110.00000000","25589.00000000","27318.00000000","26992.00000000","26922.00000000","26512.00000000","25983.00000000","26501.00000000","24299.00000000","24379.00000000","25618.00000000","25466.00000000","25146.00000000","25544.00000000","26323.00000000","28256.00000000","28804.00000000","30387.00000000","33098.00000000","27587.00000000","26043.00000000","26664.00000000","28278.00000000","28824.00000000","30646.0000000000"],"v":["1335.18050000","1321.87430000","1354.69020000","1286.95100000","1328.99090000","1354.26320000","2112.08770000","1313.62330000","1318.58630000","1413.33130000","1339.81370000","1514.41710000","1344.57440000","1644.92260000","1378.02350000","1565.08930000","1405.19770000","1376.22650000","1313.04360000","1269.46550000","1323.36560000","1370.56650000","976.53950000","334.33420000","249.72250000","495.70470000","626.85520000","617.49670000","651.14870000","631.91010000","565.46650000","699.44360000","927.40540000","606.83520000","609.81560000","695.68010000","598.44040000","626.43350000","278.83150000","211.71120000","303.99500000","513.09060000","551.05060000","464.11970000","467.95170000","513.90370000","321.08990000","277.21640000","307.42580000","273.33970000","439.34400000","453.13370000","476.81780000","475.98530000","478.23830000","529.49670000","357.58550000","296.98090000","459.58320000","293.15610000","587.24600000","660.19230000","550.21020000","240.19080000"],"s":"ok"}'
        
        dic = {"btc":btc,"eth":eth,"ltc":ltc,"bch":bch}
        return dic[self.coin]
    def excel(self):

        r = json.loads(self.data())
        t ,c , o, l, h ,volume = r['t'][::-1], r['c'][::-1], r['o'][::-1] ,r['l'][::-1] ,r['h'][::-1] ,r['v'][::-1]

        for index, i in enumerate(t):
            d = datetime.fromtimestamp(i)
            d = str(d).replace("00:00:00","")
            hp ,lp, op, cp ,v= int(float(h[index])), int(float(l[index])), int(float(o[index])), int(float(c[index])), int(float(volume[index]))
            print(d, op, cp, hp, lp, v)
            self.table.write(index + 1,0,d)
            self.table.write(index + 1,1,op)
            self.table.write(index + 1,2,cp)
            self.table.write(index + 1,3,hp)
            self.table.write(index + 1,4,lp)
            self.table.write(index + 1,5,v)

        

if __name__ == "__main__":
    l = ["btc","eth","bch","ltc"]
    for i in l:
        bb = Btcbox(i)
        bb.excel()
    data.save("btcbox" + '.xls')