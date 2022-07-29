# Initial imports
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
        
        """
        if(envpath == None):
            load_dotenv()
        else:
            load_dotenv(envpath)
        self._alpaca_api_key = os.getenv("ALPACA_API_KEY")       
        self._alpaca_secret_key = os.getenv("ALPACA_SECRET_KEY")
        
        
    
    def get_cryptos_price(self, urls:{}) -> {}:
        responsedic = {}
        for url in urls:            
            response = requests.get(urls[url])
            responsedic[url] =  response.json()           
            
        return responsedic
    
    
    def get_alpca_bars(self,tickers: [],timeframe: str,startdate:str = None,enddate: str = None) -> DataFrame:
        alpaca = tradeapi.REST(
            self._alpaca_api_key,
            self._alpaca_secret_key,
            api_version = "v2")
        
        df = alpaca.get_bars(tickers,
                            timeframe,
                            startdate,
                            enddate).df
        return df
                               
        
        
        
        
        
        
    
    