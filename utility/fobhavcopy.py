#import datehelper as datehandler
from . import datehelper as datehandler
from . import csvhelper as csvhandler
from os import listdir, path
from jugaad_data.nse import bhavcopy_fo_save
from datetime import date, timedelta

default_folder='./reports'
fo_bhavcopies = csvhandler.get_fo_csv_files(default_folder)

def get_fo_bhavcopy(dt:date,default_folder='./reports')->path:
    """For the given date fetch the fo bhav copy. If it is already present 
    return the file path. Else download and return the file path
    Return none on error/holiday
    """
    if datehandler.is_holiday(dt):
        print(f"holiday on {dt.isoformat()}")
        return None

    
    for bhav_copy in fo_bhavcopies:
        if dt == csvhandler.get_eod_report_date(bhav_copy):
            print(f"Bhav copy exists for {dt.isoformat()}")
            return bhav_copy
    
    try:
        print(f"Downloading Bhav copy for {dt.isoformat()}")
        file_str_path = bhavcopy_fo_save(dt,default_folder)
        refresh_fo_bhavcopies()
        return path.abspath(file_str_path)
    except:
        return None

def get_fo_bhav_copies(from_date:date, to_date:date, folder=default_folder)->list:
    one_day_delta = timedelta(days = 1)
    bhavcopy_files = []
    while from_date <= to_date:
        file = get_fo_bhavcopy(from_date,folder)
        if file:
            bhavcopy_files.append(file)
        from_date = from_date + one_day_delta

    return bhavcopy_files

def refresh_fo_bhavcopies():
    fo_bhavcopies = csvhandler.get_fo_csv_files(default_folder)

if __name__ == '__main__':
    from_date = date(2022,4,1)
    to_date = date(2022,5,4)
    files = get_fo_bhav_copies(from_date,to_date)
    for f in files:
        print(f)
    