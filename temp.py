
import utility.csvhelper as csvhandler
import pandas as pd
import utility.lotsize as lots
import utility.oidata as oi

report_folder = './reports'
test_sym = 'TCS'

fo_bhavcopies = csvhandler.get_fo_csv_files(report_folder)

for f in fo_bhavcopies:
    print(f)

test_bhavcopy = fo_bhavcopies[0]
data = oi.get_bhav_oi_data(test_bhavcopy,test_sym)
print(lots.lot_size[test_sym])
print(data.call_oi)
