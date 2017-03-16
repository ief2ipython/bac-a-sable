#!/usr/bin/python3

from yahoo_finance import Share
import sqlite3
import datetime


conn = sqlite3.connect('stocks.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS stocks (
                       stock_date datetime, ticker text, open real, close real, high real, low real, volume long, PRIMARY KEY (stock_date, ticker))''')

# - get today data
now = datetime.datetime.now()
today = "{0}-{1}-{2}".format(now.year,str(now.month).zfill(2),str(now.day).zfill(2))

with open("../data/nasdaq107list.csv", "r") as f:
    content = f.readlines()

for ticker in content:
    ticker = ticker.rstrip('\n')
    try:
        yahoo= Share(ticker)
    except AttributeError:
        pass

    stock = (yahoo.get_historical('2007-01-01', today))

    for st in stock :
        row= []
        print (st)
        st_symbol = st['Symbol']
        row.append(st_symbol)
        st_date   = st['Date']
        row.append(st_date)
        st_open   = st['Open']
        row.append(st_open)
        st_close  = st['Close']
        row.append(st_close)
        st_high   = st['High']
        row.append(st_high)
        st_low    = st['Low']
        row.append(st_low)
        st_volume = st['Volume']
        row.append(st_volume)
        try:
            sql= '''INSERT INTO stocks(stock_date,ticker,open,close,high,low,volume)
                       VALUES (?,?,?,?,?,?,?)'''
            c.execute(sql,row)
        except sqlite3.IntegrityError:
            pass
        conn.commit()
conn.close()

