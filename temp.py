

from datetime import date


import utility.fobhavcopy as foreport
import utility.csvhelper as csvhand
import utility.oidata as oi
import matplotlib.pyplot as plt
import utility.lotsize as lot
import pandas as pd
import numpy as np

dt = date.today()
report_folder = './reports'
test_sym = 'BHARTIARTL'


from_date = date(2022,2,1)
to_date = date(2022,5,5)
files = foreport.get_fo_bhav_copies(from_date,to_date)
dates = list(map(lambda x : csvhand.get_eod_report_date(x).strftime('%d/%m'),files))

data = []

lot_size = lot.lot_size[test_sym]
print(lot_size)

for f in files:
    oi_data = oi.get_bhav_oi_data(f,test_sym)
    if not len(oi_data) == 0:
        data.append(oi_data)
  
call_oi_ch = [x[1]/lot_size for x in data]
put_oi_ch = [x[3]/lot_size for x in data]


# plt.bar(dates,call_oi_ch)
# plt.xticks(rotation=90)
# plt.show()


# df  = pd.DataFrame({'Call oi ch':call_oi_ch,'Put oi ch':put_oi_ch},index=dates)
# print(df.head())
# df.plot.bar(rot=0, color={"Call oi ch": "green", "Put oi ch": "red"})
# plt.show()

x_axis = np.arange(len(dates))

# Multi bar Chart

plt.bar(x_axis -0.2, call_oi_ch, width=0.4, label = 'call oi ch')
plt.bar(x_axis +0.2, put_oi_ch, width=0.4, label = 'put oi ch')

# Xticks
plt.grid(True, color = "grey", linestyle='dashed')
plt.xticks(x_axis, dates)
plt.xticks(rotation=90)

# Add legend

plt.legend()

# Display

plt.show()