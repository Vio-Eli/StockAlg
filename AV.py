from alpha_vantage.timeseries import TimeSeries
import pandas as pd
from datetime import datetime
from io import BytesIO
import base64
import gc
import config

def incoming_data(stock, data_type):

    #uhhh, just leave this for now. ill make this nice sooner or later...
    """
    if data_type == 'open':
        data_typer = '1. open'
    elif data_type == 'high':
        data_typer = '2. high'
    elif data_type == 'low':
        data_typer = '3. low'
    elif data_type == 'close':
        data_typer = '4. close'
    elif data_type == 'adj close':
        data_typer = '5. adjusted close'
    elif data_type == 'volume':
        data_typer = '6. volume'
    elif data_type == 'dividend amt':
        data_typer = '7. dividend amount'
    elif data_type == 'split coefficient':
        data_typer = '8. split coefficient'
    """

    data_type_dict = {'open': '1. open', 'high': '2. high', 'low': '3. low', 'close': '4. close', 'adj close': '5. adjusted close', 'volume': '6.volume', 'dividend amt': '7. dividend amount', 'split coefficient': '8. split coefficient'}

    data_typer = data_type_dict[str(data_type)]
    

    ts = TimeSeries(key = '1ORS1XLM1YK1GK9Y')
    data_old = ts.get_daily_adjusted(stock, outputsize = 'full')

    #print(data_old) #FIXME Debug. BEWARE! WALL OF TEXT!

    date_old = []
    close_old = []

    open_old = []
    cls_old = []

    for keys_old in data_old[0].keys():
        if int(keys_old[0:4]) > 1970:
            date_old.append(pd.to_datetime(keys_old))
            close_old.append(float(data_old[0][keys_old][str(data_typer)]))
            
            open_old.append(float(data_old[0][keys_old]['1. open']))
            cls_old.append(float(data_old[0][keys_old][str('4. close')]))


    df_old = pd.DataFrame({'date': date_old, str(data_type): close_old})
    df_open = pd.DataFrame({'date': date_old, 'open': open_old})
    df_close = pd.DataFrame({'date': date_old, 'close': cls_old})


    df_old.sort_values('date', ascending = False, inplace = True)
    df_open.sort_values('date', ascending = False, inplace = True)
    df_close.sort_values('date', ascending = False, inplace = True)


    df_old['date'] = pd.to_datetime(df_old['date'])
    df_open['date'] = pd.to_datetime(df_open['date'])
    df_close['date'] = pd.to_datetime(df_close['date'])
    

    df_old.set_index(['date'], inplace = True)
    df_open.set_index(['date'], inplace = True)
    df_close.set_index(['date'], inplace = True)

    if len(df_open) != len(df_close):
        print("ERROR: Length of data differs")
    
    #df_close_lst = df_close['close'].values.tolist()
    #df_open_lst = df_open['open'].values.tolist()
    #difflist = [df_close_lst[i] - df_open_lst[i] for i in range(len(df_open))]

    #difflist = pd.concat([df_open, df_close])
    difflist = pd.merge(df_open, df_close, left_index=True, right_index=True)
    difflist['diff'] = difflist['close'] - difflist['open']
           

    return df_old, difflist


# misc keys:
# 3Q1BOM6NBZ4QGCGW
# 1ORS1XLM1YK1GK9Y
    