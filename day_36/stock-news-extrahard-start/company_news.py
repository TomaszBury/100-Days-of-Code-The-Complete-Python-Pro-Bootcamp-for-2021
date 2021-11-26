from bs4 import BeautifulSoup
from newsapi.newsapi_client import NewsApiClient

COMPANY_NAME = "Tesla Inc"
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

API_KEY_NEWS = "de225d1262664c1da509e6bcb398c8e2"

# Init
newsapi = NewsApiClient(api_key=API_KEY_NEWS)

# print(all_articles['articles'])
#
# the_end_of_the_look = 1
#
# while the_end_of_the_look >= 0:
#     print(all_articles['articles'][the_end_of_the_look]['title'])
#     print(all_articles['articles'][the_end_of_the_look]['description'])
#     soup = BeautifulSoup(all_articles['articles'][the_end_of_the_look]['description'], features="html.parser")
#     print(soup.getText())
#     the_end_of_the_look -= 1


def get_news(about: str, how_many: int) -> str:
    all_articles = newsapi.get_everything(q=about, language='en')
    title_and_description = ""
    while how_many >= 0:
        title_and_description += "Headline: "
        title_and_description += all_articles['articles'][how_many]['title']
        title_and_description += " \n"

        soup_description = BeautifulSoup(all_articles['articles'][how_many]['description'], features="html.parser")
        title_and_description += "Brief: "
        title_and_description += soup_description.getText()
        title_and_description += " \n"
        how_many -= 1

    return title_and_description
