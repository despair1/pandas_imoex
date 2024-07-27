import requests
import pandas as pd
from io import StringIO


def get_candlestick_data(ticker, interval='24', start_date=None, end_date=None):
    """
    Fetch candlestick data for a specific stock ticker.

    :param ticker: Stock ticker symbol
    :param interval: Candlestick interval (e.g., '10' for 10 minutes, '24' for daily, etc.)
    :param start_date: Start date in 'YYYY-MM-DD' format (optional)
    :param end_date: End date in 'YYYY-MM-DD' format (optional)
    :return: List of dictionaries containing OHLCV data
    """
    # Define the base URL for the MOEX API
    url = f"https://iss.moex.com/iss/engines/stock/markets/bonds/securities/{ticker}/candles.csv"

    # Define the parameters for the API request
    params = {
        'interval': interval
    }

    if start_date:
        params['from'] = start_date
    if end_date:
        params['till'] = end_date

    # Make a GET request to the MOEX API
    response = requests.get(url, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        csv_data = StringIO(response.text)
        df = pd.read_csv(csv_data,sep=";",header=1)
        # print(df)
        return df
    else:
        print(f"Failed to retrieve data: {response.status_code} {ticker}")
        return None


# Example usage
ticker = "SU26212RMFS9"  # Replace with the ticker symbol you are interested in
interval = '24'  # Daily interval
start_date = '2023-01-01'  # Start date in 'YYYY-MM-DD' format
end_date = '2023-10-01'  # End date in 'YYYY-MM-DD' format (optional)

# candlestick_data = get_candlestick_data(ticker, interval, start_date, end_date)
# print(candlestick_data)
# print(candlestick_data.dtypes)