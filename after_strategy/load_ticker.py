import after_hours

with open("../data/nasdaq107list.csv", "r") as f:
    content = f.readlines()
#print (content)

for ticker in content:
    ticker = ticker.rstrip('\n')
    try:
        trades = after_hours.ah_all(ticker)[2]
        open = trades[0]
        close = trades[-1]
        sorted_trades = sorted(trades)
        low = sorted_trades[0]
        high= sorted_trades[-1]
        if open>close:
            trend = "bearish"
        else:
            trend = "bullish"
        print (ticker,high,open,close,low,trend)
    except (TypeError, IndexError):
        print (ticker, -1,-1,-1,-1,-1)

