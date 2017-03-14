from yahoo_finance import Share
import sqlite3


conn = sqlite3.connect('stocks.db')
c = conn.cursor()
c.execute('''CREATE TABLE stocks (
                       stock_date datetime, ticker text, open real, close real, high real, low real, volume long, PRIMARY KEY (stock_date, ticker)''')

with open("../data/nasdaq107list.csv", "r") as f:
    content = f.readlines()

for ticker in content:
    ticker = ticker.rstrip('\n')
    yahoo= Share(ticker)
    a = (yahoo.get_historical('2017-03-10', '2017-03-13'))

    for i in a :
        print (i)
        print(i['Symbol'])

