import ccxt
import pandas_ta as ta
from binance import Client, ThreadedDepthCacheManager, ThreadedWebsocketManager
from CryptoIndicator import RSI, ADX, MACD

  
def main():
    " Dropdown Selection DEMO"
    symbols = ["ETH/USDT", "BNB/USDT", "BCT/USDT", "KAVA/USDT", "AVAX/USDT",
     "SOL/USDT", "ADA/USDT", "ENJ/USDT", "DOGI/USDT", "SHIB/USDT"]

    inp = input("Select Coin (COIN/USDT): ")


main()


