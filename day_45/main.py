from bs4 import BeautifulSoup
import requests

response = requests.get(("https://news.ycombinator.com/"))

# print(response.text)
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "html.parser")

article_tag = soup.find_all(name="a", class_="titlelink")

for article in article_tag:
    print(article.getText())

print(f"\nLinks:\n")

for article in article_tag:
    print(article.get("href"))

print(f"\nUp Vote:\n")

article_upvote = soup.find_all(name="span", class_="score")
for upvote in article_upvote:
    print(upvote.getText())
