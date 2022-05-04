from os import listdir, path
from os.path import isfile, join
from datetime import date, datetime
import re

__all__ = ['get_fo_csv_files','get_eod_report_date',]

def get_csv_files(fpath:path)->list:
    """
    Private Function to fetch all csv files in the given path
    """
    onlycsvFiles = [path.abspath(join(fpath, f)) for f in listdir(fpath) if isfile(join(fpath, f)) and  f.endswith(".csv")]
    return onlycsvFiles

def is_fo_report_file(file_name:str)->bool:
    "check if file name is in fo report format foddmmmyyyybhav"
    search_exp = 'fo([0-9]{2}[a-zA-Z]{3}[0-9]{4}bhav.csv)'
    res = re.search(search_exp,file_name)
    if res:
        return True
    else:
        return False

def get_eod_report_date(file_name):
    "extract report date from file name: foddmmmyyyybhav"
    search_exp = '([0-9]{2}[a-zA-Z]{3}[0-9]{4})'
    res = re.search(search_exp,file_name)
    if res:
        return datetime.strptime(res.group(0),"%d%b%Y").date()
    else:
        return None

def get_fo_csv_files(fpath:path)->list:
    "fetch all fo bhav copy in the provided folder"

    csv_files = get_csv_files(fpath)
    fo_csv_files = list(filter(is_fo_report_file,csv_files))
    return fo_csv_files

if __name__ == '__main__':
    report_files = get_csv_files('./reports')
    for report in report_files:
        print(report)
    print('-*-' * 10)
    fo_report = get_fo_csv_files('./reports')
    for report in fo_report:
        print(report)

        
    