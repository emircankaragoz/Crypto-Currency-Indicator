import ccxt, yfinance
import pandas_ta as ta
import pandas as pd
import time

api_key = "JMG85Zm3XoOngTsyQZi4Wxx4Q4sLwEhfOTzMEi9HQPJtwiajLpux7CPnGMgCGFao"
secret_key= "DjUL6175P4L5GXyWiLKTlg3c6qYNmJCKwQhLTHu8jWaZQmWZVamQ6290DtzrzMBj"

""" CCXT, farkli kripto işlem veri kütüphanelerine bağlanmak için ortak bir arayüz sağlayan
 dünyanin önde gelen açik kaynak kütüphanelerinden biri """
account_binance = ccxt.binance({
    "apiKey": f"{api_key}",
    "secret": f"{secret_key}",
    "enableRateLimit": True,
    "options": { 
        "defaultType": "spot"
    }
})
account_binance = ccxt.binance({ 'options': { 'adjustForTimeDifference': True }})

exchange = account_binance

def take_bars_rsi(coin):
    bars = exchange.fetch_ohlcv(coin,timeframe="5m",limit=500)
    df = pd.DataFrame(bars,columns=['time','open','high','low','close','volume'])

    return df


def RSI(coin):
    bars = exchange.fetch_ohlcv(coin,timeframe="5m",limit=500)
    df = pd.DataFrame(bars,columns=['time','open','high','low','close','volume'])

   

    """ RSI (Relative Strenght Index) => Bir hareket göstergesidir. MA (Moving Avarage) baglidir. """
    rsi = df.ta.rsi()

    return rsi

def ADX(coin):
    bars = exchange.fetch_ohlcv(coin,timeframe="5m",limit=500)
    df = pd.DataFrame(bars,columns=['time','open','high','low','close','volume'])

    """ avarage directional index (adx) =>  adx ema (exponentional moving avarage)'a bagli trend gücünü ölçmek için kullaniliyor"""
    adx = df.ta.adx()

    return adx

def MACD(coin):
    bars = exchange.fetch_ohlcv(coin,timeframe="5m",limit=500)
    df = pd.DataFrame(bars,columns=['time','open','high','low','close','volume'])

    """ MACD( Moving Av. Convergence/Divergence) => Trendi takip eden bir momentumdur. """
    macd = df.ta.macd(fast=14,slow=20)

    return macd

