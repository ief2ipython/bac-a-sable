from yahoo_finance import Share

yahoo= Share('AMZN')
print (yahoo.get_open())
print (yahoo.get_historical('2007-01-01', '2017-03-06'))
