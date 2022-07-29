# Initial imports
import os
import requests
from pandas import DataFrame
from pathlib import Path
from dotenv import load_dotenv
import alpaca_trade_api as tradeapi

class APIcalls:
    def __init__(self, envpath: Path = None):
        """
        APIcalls constructor, load's environment and initializes key variables
        envpath : specifies path of environment file 
        """
        if(envpath == None):
            load_dotenv()
        else:
            load_dotenv(envpath)
        self._alpaca_api_key = os.getenv("ALPACA_API_KEY")       
        self._alpaca_secret_key = os.getenv("ALPACA_SECRET_KEY")
        
        
    
    def get_cryptos_price(self, urls:{}) -> {}:
        """
        get_cryptos_price fetches Crypto data e.g. prices, volume using request library
        urls : dictionary of {<Crypto symbol> : <url to make request call>}
        returns: dictionary of {<Crypto symbol> : <response json object}
        """
        responsedic = {}
        for url in urls:            
            response = requests.get(urls[url])
            responsedic[url] =  response.json()           
            
        return responsedic
    
    
    def get_alpca_bars(self,tickers: [],timeframe: str,startdate:str = None,enddate: str = None) -> DataFrame:
        """
        get_alpca_bars uses alpca sdk to get tickers bars.
        
        tickers : list of string that represents tickers symbols
        timeframe : represents duration for which data is required e.g. "1Day"
        startdate :  start date
        enddate : end date        
        return : DataFrame containing ticker historical data fetched from alpaca api
        """
        alpaca = tradeapi.REST(
            self._alpaca_api_key,
            self._alpaca_secret_key,
            api_version = "v2")
        
        df = alpaca.get_bars(tickers,
                            timeframe,
                            startdate,
                            enddate).df
        return df
                               
        
        
        
        
        
        
    
    