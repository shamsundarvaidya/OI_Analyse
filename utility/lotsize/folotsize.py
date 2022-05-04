import pandas as pd
import os

folder_name = os.path.dirname(__file__)


lot_size = {}

def update_lot_sizes():
    "Function to refresh the lot size data from csv file"
    df = pd.read_csv(os.path.abspath(os.path.join(folder_name,'fo_mktlots.csv')))
    for index, row in df.iterrows():
        sym = str(row[0]).rstrip()
        lot = row[1]
        lot_size[sym] = lot
    

if len(lot_size) == 0:
    update_lot_sizes()

if __name__ == '__main__':
    update_lot_sizes()
    print(lot_size.keys())
    print(lot_size.get('TCS'))
    