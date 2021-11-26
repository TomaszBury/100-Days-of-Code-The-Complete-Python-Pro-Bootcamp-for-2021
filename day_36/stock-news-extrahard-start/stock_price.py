import requests
import datetime

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


# print(data['Monthly Time Series'])
# print(data['Monthly Time Series'].keys())


def current_date(less=1):
    yesterday_date = datetime.datetime.now()
    date = yesterday_date.strftime("%Y") + "-" \
           + yesterday_date.strftime("%m") + "-" \
           + str(int(yesterday_date.strftime("%d")) - less)
    return date


# for day in data['Monthly Time Series'].values():
#     # print(f'open:{day["1. open"]}, close:{day["4. close"]}')
#     stock_price_open = float(day["1. open"])
#     stock_price_close = float(day["4. close"])
#     delta_on_stock = stock_price_open - stock_price_close
#     abs_increase_decrease = abs(delta_on_stock) / stock_price_open
#     # if abs_increase_decrease >= 0.05:
#     #     print("Get News")

def get_percentage_change():
    date_not_found = True
    next_date = 0
    percentage_change = ""

    while date_not_found:
        date = current_date(next_date)
        for key, value in data['Monthly Time Series'].items():
            if key == date:
                # print(f"key:{key}")
                stock_price_open = float(value["1. open"])
                stock_price_close = float(value["4. close"])
                delta_on_stock = stock_price_open - stock_price_close
                abs_increase_decrease = abs(delta_on_stock) / stock_price_open
                # print(f'abs_increase_decrease: {abs_increase_decrease:.2f}')
                percentage_change = f'{abs_increase_decrease * 100:.2f}%'
                # print(percentage_change)
                date_not_found = False
                break
        next_date += 1

    return percentage_change
