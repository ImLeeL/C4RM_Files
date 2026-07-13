import yfinance as yf
import pandas as pd

def YahooData2returns(YahooData):
    close_price = YahooData['Close']
    pricevec = close_price.values
    returns = pricevec[1:] / pricevec[:-1] - 1

    return returns
