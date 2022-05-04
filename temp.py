
import utility.csvhelper as csvhandler
import pandas as pd
import utility.lotsize as lots
import utility.oidata as oi
from jugaad_data.nse import bhavcopy_save, bhavcopy_fo_save
from datetime import date, timedelta 
from os import path
import time
import utility.datehelper as datefunc



dt = date.today()
report_folder = './reports'
test_sym = 'TCS'

# fo_bhavcopies = csvhandler.get_fo_csv_files(report_folder)

# for f in fo_bhavcopies:
#     print(csvhandler.get_eod_report_date(f))

# test_bhavcopy = fo_bhavcopies[0]
# data = oi.get_bhav_oi_data(test_bhavcopy,test_sym)
# print(lots.lot_size[test_sym])
# print(data.call_oi)


