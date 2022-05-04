

from datetime import date


import utility.fobhavcopy as foreport
import utility.csvhelper as csvhand
import utility.oidata as oi
import matplotlib.pyplot as plt
import utility.lotsize as lot

dt = date.today()
report_folder = './reports'
test_sym = 'TCS'


from_date = date(2022,2,1)
to_date = date(2022,5,4)
files = foreport.get_fo_bhav_copies(from_date,to_date)
dates = list(map(lambda x : csvhand.get_eod_report_date(x).strftime('%d-%m-%y'),files))

data = []

lot_size = lot.lot_size[test_sym]
print(lot_size)

for f in files:
    oi_data = oi.get_bhav_oi_data(f,test_sym)
    if not len(oi_data) == 0:
        data.append(oi_data)
  
call_oi_ch = [x[1]/lot_size for x in data]


plt.bar(dates,call_oi_ch)
plt.xticks(rotation=90)
plt.show()