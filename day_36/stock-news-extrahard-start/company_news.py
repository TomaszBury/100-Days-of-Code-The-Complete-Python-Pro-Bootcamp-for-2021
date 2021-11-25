from newsapi.newsapi_client import NewsApiClient

COMPANY_NAME = "Tesla Inc"
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

API_KEY_NEWS = "de225d1262664c1da509e6bcb398c8e2"


# Init
newsapi = NewsApiClient(api_key=API_KEY_NEWS)

# /v2/everything
all_articles = newsapi.get_everything(q=COMPANY_NAME,
                                      domains='reuters.com',
                                      language='en')

print(all_articles['articles'])

the_end_of_the_look = 4

while the_end_of_the_look >= 0:
    print(all_articles['articles'][the_end_of_the_look]['title'])
    the_end_of_the_look -=1

