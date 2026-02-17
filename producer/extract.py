import requests
from config import logger,headers,url


def connect_to_api():
    stocks = ['TSLA', 'MSFT','GOOGL']
    json_response=[]
    for stock in range(0,len(stocks)):
        querystring = {"function":"TIME_SERIES_INTRADAY",
                       "symbol":f"{stocks[stock]}",
                       "outputsize":"compact",
                       "interval":"5min",
                       "datatype":"json"
                       }

        try:
            response = requests.get(url, headers=headers, params=querystring)

            response.raise_for_status()

            data=response.json()

            logger.info(f"Stocks {stocks[stock]} succesfuly loaded")

            json_response.append(data)

        except requests.exceptions.RequestException as e:
            logger.error(f"Error on stock: {e}")
            break
    return json_response

def extract_json(response):
    records = []
    
    for data in response:
        try:
            symbol = data['Meta Data']['2. Symbol']
            time_series = data['Time Series (5min)']
        except (KeyError, TypeError):
            continue  # skip invalid entries
            
        for date_str, metrics in time_series.items():
            try:
                record = {
                    "symbol": symbol,
                    "date": date_str,
                    "open": metrics["1. open"],
                    "high": metrics["2. high"],
                    "low": metrics["3. low"],
                    "close": metrics["4. close"],
                }
                records.append(record)
            except KeyError:
                continue  # skip broken candles
    
    return records