
import utility.csvhelper as csvhandler
import pandas as pd
import utility.lotsize as lots
import utility.oidata as oi
from jugaad_data.nse import bhavcopy_save, bhavcopy_fo_save


report_folder = './reports'
test_sym = 'TCS'

fo_bhavcopies = csvhandler.get_fo_csv_files(report_folder)

for f in fo_bhavcopies:
    print(f)

test_bhavcopy = fo_bhavcopies[0]
data = oi.get_bhav_oi_data(test_bhavcopy,test_sym)
print(lots.lot_size[test_sym])
print(data.call_oi)

import requests, zipfile, io
r = requests.get('https://www1.nseindia.com/content/historical/DERIVATIVES/2022/MAY/fo02MAY2022bhav.csv.zip')
z = zipfile.ZipFile(io.BytesIO(r.content))
z.extractall("./reports")