
import utility.csvhelper as csvhandler
import pandas as pd
import utility.lotsize as lots

report_folder = './reports'
test_sym = 'TCS'

fo_bhavcopies = csvhandler.get_fo_csv_files(report_folder)

for f in fo_bhavcopies:
    print(f)

test_bhavcopy = fo_bhavcopies[0]
df = pd.read_csv(test_bhavcopy)

df_ce_filter = (df['SYMBOL'] == test_sym) & (df['INSTRUMENT'] == 'OPTSTK') & (df['OPTION_TYP'] == 'CE')
df_pe_filter = (df['SYMBOL'] == test_sym) & (df['INSTRUMENT'] == 'OPTSTK') & (df['OPTION_TYP'] == 'PE')

call_data = df.loc[df_ce_filter]

call_oi = call_data['OPEN_INT'].sum(axis=0)
call_oi_change = call_data['CHG_IN_OI'].sum(axis=0)

print(call_oi)
print(call_oi_change)
print(lots.lot_size[test_sym])
