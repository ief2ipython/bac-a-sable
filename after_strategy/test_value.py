#!/usr/bin/env python3

import after_hours

from urllib.parse import parse_qs
from math import *

ticker ="ibm"

trades= after_hours.ah_all(ticker)[2]
open=trades[0]
close=trades[-1]
sorted_trades=sorted(trades)
low =sorted_trades[0]
high=sorted_trades[-1]
if open>close:
    trend = "bearish"
else:
    trend = "bullish"
print (high,open,close,low,trend)


#print (all_stock[2]

def bs_call(S,X,T,r,sigma):
    d1 = (log(S/X)+(r+sigma*sigma/2.)*T)/(sigma*sqrt(T))
    d2 = d1-sigma*sqrt(T)
    return S*CND(d1)-X*exp(-r*T)*CND(d2)

def CND(X):
    (a1, a2, a3, a4, a5) = (0.31938153, -0.356563782, 1.781477937, -1.821255978, 1.330274429)
    L = abs(X)
    K=1.0/(1.0+0.2316419*L)
    w=1.0-1.0/sqrt(2*pi)*exp(-L*L/2.)*(a1*K+a2*K*K+a3*pow(K,3)+a4*pow(K,4)+a5*pow(K,5))
    if X<0:
        w = 1.0-w
    return w

#bs=bs_call(40,42,0.5,0.1,0.2)
#print(bs)
#zero=CND(0)
#print (zero)
#one_percent=CND(-2.326)
#print (one_percent)
#max_percent=CND(1.645)
#print(max_percent)




