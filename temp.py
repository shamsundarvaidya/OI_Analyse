
import utility.csvhelper as csvhandler
import pandas as pd
import utility.lotsize as lots
import utility.oidata as oi
from jugaad_data.nse import bhavcopy_save, bhavcopy_fo_save
from datetime import date, timedelta 
from os import path
import time
import utility.datehelper as datefunc

def get_max_date()->date:
    localtime = time.localtime(time.time())
    hour = localtime.tm_hour
    cur_date = date.today()
    if hour < 19 :
        return cur_date - timedelta(days=1)
    else:
        return cur_date


def get_fo_bhavcopy(dt:date,default_folder='./reports')->path:
    """For the given date fetch the fo bhav copy. If it is already present 
    return the file path. Else download and return the file path
    Return none on error/holiday
    """
    if datefunc.is_holiday(dt):
        return None

    fo_bhavcopies = csvhandler.get_fo_csv_files(default_folder)

    for bhav_copy in fo_bhavcopies:
        if date == csvhandler.get_eod_report_date(bhav_copy):
            return bhav_copy
    
    try:
        file_str_path = bhavcopy_fo_save(dt,default_folder)
        return path.abspath(file_str_path)
    except:
        return None
    

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

print(get_fo_bhavcopy(dt))

