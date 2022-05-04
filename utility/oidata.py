from collections import namedtuple as nd
import pandas as pd


OI_data = nd('OI_data',('call_oi', 'call_oi_change',
                        'put_oi', 'put_oi_change'))

OI_data.__doc__ = "named tuple to hold OI data : \
    call_oi,call_oi_change,put_oi, put_oi_change"

def get_bhav_oi_data(fpath,company_sym)->tuple:
    "Extract OI data from bhav copy. Returns a tuple of four data"
    df = pd.read_csv(fpath)

    df_ce_filter = (df['SYMBOL'] == company_sym) & (df['INSTRUMENT'] == 'OPTSTK') & (df['OPTION_TYP'] == 'CE')
    df_pe_filter = (df['SYMBOL'] == company_sym) & (df['INSTRUMENT'] == 'OPTSTK') & (df['OPTION_TYP'] == 'PE')

    call_data = df.loc[df_ce_filter]
    call_oi = call_data['OPEN_INT'].sum(axis=0)
    call_oi_ch = call_data['CHG_IN_OI'].sum(axis=0)

    put_data = df.loc[df_pe_filter]
    put_oi = put_data['OPEN_INT'].sum(axis=0)
    put_oi_ch = put_data['CHG_IN_OI'].sum(axis=0)

    return OI_data(call_oi,call_oi_ch,put_oi,put_oi_ch)


if __name__ == '__main__':
    data = get_bhav_oi_data('./reports/fo27APR2022bhav.csv',"TCS")
    print(data)

