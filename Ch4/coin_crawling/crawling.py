import pyupbit
import sqlite3

def get_lists():
    coin_lists = pyupbit.get_tickers(fiat='KRW')
    return coin_lists

def get_price(list):
    # price_now = pyupbit.get_current_price(['KRW-BTC', 'KRW-ETH'])
    price_now = pyupbit.get_current_price(list)
    return price_now

def crawling():
    ticker = 'KRW-BTC'
    interval = 'minute1'
    to = '2022-10-04 16:00'
    count = 200
    price_now = pyupbit.get_ohlcv(ticker=ticker, interval=interval, to=to, count=count)

    db_path = 'coin.db'
    conn = sqlite3.connect(db_path, isolation_level=None)
    price_now.to_sql('BTC', conn, if_exists='append')

    conn.close()