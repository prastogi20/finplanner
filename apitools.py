# Initial imports
import os
import requests
from pandas import DataFrame
from pathlib import Path
from dotenv import load_dotenv
import alpaca_trade_api as tradeapi

class APIcalls:
    """
    A python class for fetching data using requests library & alpaca api 
    
    Constructor : initalizes & load environment
                  params: envpath - optional parameter for environment file Path
    ...
    
    Functions    
    ----------
    get_cryptos_price :fetches data e.g. prices, volume using request library
                       params : urls - dictionary of { <symbol> : <url to make request call>}
                       returns: dictionary of {<symbol> : <response json object}
                       
    get_alpaca_bars : Create the Alpaca API object & Get tickers data by using alpca sdk method get_bars
                      params: tickers - list of string that represents tickers symbols
                              timeframe - represents duration for which data is required e.g. "1Day"
                              startdate - string type, represents start date
                              enddate - string type, represents end date        
                      return : DataFrame containing ticker historical data fetched from alpaca api
    """
    def __init__(self, envpath: Path = None):     
        if(envpath == None):
            load_dotenv()
        else:
            load_dotenv(envpath)
        
        # Set Alpaca API key and secret
        self._alpaca_api_key = os.getenv("ALPACA_API_KEY")       
        self._alpaca_secret_key = os.getenv("ALPACA_SECRET_KEY")
        
        
    
    def get_data_request(self, urls:{}) -> {}:
        """
        get_cryptos_price : fetches data e.g. prices, volume using request library
                            params: urls - dictionary of { <symbol> : <url to make request call>}
                            returns: dictionary of {<symbol> : <response json object}
        """
        responsedic = {}
        for url in urls:            
            response = requests.get(urls[url])
            responsedic[url] =  response.json()           
            
        return responsedic
    
    
    def get_alpaca_bars(self,tickers: [],timeframe: str,startdate:str = None,enddate: str = None) -> DataFrame:
        """
        get_alpaca_bars Create the Alpaca API object & Get tickers data by using alpca sdk method get_bars
        
        tickers : list of string that represents tickers symbols
        timeframe : represents duration for which data is required e.g. "1Day"
        startdate :  start date
        enddate : end date        
        return : DataFrame containing ticker historical data fetched from alpaca api
        """
        
        # Create the Alpaca API object
        alpaca = tradeapi.REST(
            self._alpaca_api_key,
            self._alpaca_secret_key,
            api_version = "v2")
        
        df = alpaca.get_bars(tickers,
                            timeframe,
                            startdate,
                            enddate).df
        return df
                               
        
        
        
        
        
        
    
    