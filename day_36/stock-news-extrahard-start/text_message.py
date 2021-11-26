from twilio.rest import Client
from company_news import get_news
from stock_price import get_percentage_change

# STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.

account_sid = 'AC5bc524185462dc297c503a96996ff8fc'
auth_token = '64d2e2d523901adcf0ffe1ffac42d5f5'
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"


def send_the_news():
    news = get_news(COMPANY_NAME, 1)
    percentage_change = get_percentage_change()
    # print(f"Change in stock price: {percentage_change},\nnews: {news}")

    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body=f"TSLA: {percentage_change},\nnews: {news}",
        from_='+12184007348',
        to='+48501509592'  # number phone
    )
