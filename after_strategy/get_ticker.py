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

    stock = (yahoo.get_historical('2017-03-17', today))

    for st in stock :
        row= []
        print (st)
        row.append(st['Date'])
        row.append(st['Symbol'])
        row.append(st['Open'])
        row.append(st['Close'])
        row.append(st['High'])
        row.append(st['Low'])
        row.append(st['Volume'])
        try:
            sql= '''INSERT INTO stocks(stock_date,ticker,open,close,high,low,volume)
                       VALUES (?,?,?,?,?,?,?)'''
            c.execute(sql,row)
        except sqlite3.IntegrityError:
            pass
        conn.commit()
conn.close()

