import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHA_VANTAGE_API_KEY = "OW6FQ5D6DZM24O9A"
url_api = "https://www.alphavantage.co/query"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

parameters_onetime_all = {
    "function": "TIME_SERIES_MONTHLY",
    "symbol": STOCK,
    "interval": "60min",
    "apikey": ALPHA_VANTAGE_API_KEY,
}

r = requests.get(url_api, params=parameters_onetime_all)
# url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={STOCK}' \
#       f'&interval=60min&apikey={ALPHA_VANTAGE_API_KEY}'
# r = requests.get(url)
data = r.json()

print(data['Monthly Time Series'])
print(data['Monthly Time Series'].keys())

for day in data['Monthly Time Series'].values():
    print(f'open:{day["1. open"]}, close:{day["4. close"]}')
    stock_price_open = float(day["1. open"])
    stock_price_close = float(day["4. close"])
    delta_on_stock = stock_price_open - stock_price_close
    abs_increase_decrease = abs(delta_on_stock) / stock_price_open
    if abs_increase_decrease >= 0.05:
        print("Get News")
