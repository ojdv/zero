import pandas
import pandas_datareader as web
def get_stock(ticker='2330.TW'):
    df=web.DataReader(ticker,'yahoow')

    df['MA20'] = df['Close'].rolling(20).mean()
    df['MA60'] = df['Close'].rolling(60).mean()
    df['MA120'] = df['Close'].rolling(120).mean()
    df['MA240'] = df['Close'].rolling(240).mean()
    return df

df_2330=get_stock(ticker='2330.TW')


