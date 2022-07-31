# Unit 5 Homework Assignment: Financial Planning 
## Background
Created two tools for financial planning 

* First tool is a personal finance planner that will allow users to visualize their savings composed by investments in shares and cryptocurrencies to assess if they have enough money as an emergency fund.

* The second tool is a retirement planning tool that will use the Alpaca API to fetch historical closing prices for a retirement portfolio composed of stocks and bonds, then run Monte Carlo simulations to project the portfolio performance at 30 years. The Monte Carlo data is used to calculate the expected portfolio returns given a specific initial investment amount.

## Solution

Run financial-planner.ipynb, for tool analysis and results.

    Created python file APITools.py, this file has a class APICalls. 

    Init signature: APIcalls(envpath: pathlib.Path = None)

    A python class for fetching data using requests library & alpaca api 

    Constructor : initalizes & load environment
                  params: envpath - optional parameter for environment file Path
    ...

    Functions    
    ----------
    get_data_request :fetches data e.g. prices, volume using request library
                       params : urls - dictionary of { <symbol> : <url to make request call>}
                       returns: dictionary of {<symbol> : <response json object}
                    
    get_alpaca_bars : Create the Alpaca API object & Get tickers data by using alpca sdk method get_bars
                      params: tickers - list of string that represents tickers symbols
                            timeframe - represents duration for which data is required e.g. "1Day"
                            startdate - string type, represents start date
                            enddate - string type, represents end date        
                      return : DataFrame containing ticker historical data fetched from alpaca api



    