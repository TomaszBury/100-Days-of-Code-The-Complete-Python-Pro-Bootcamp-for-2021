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

article_upvotes = [int(score.getText().split(" ")[0]) for score in soup.find_all(name="span", class_="score")]

print(article_upvotes)
largest_number_of_upvotes = max(article_upvotes)
index_of_largest_number_of_upvotes = article_upvotes.index(largest_number_of_upvotes)
print(article_upvotes[index_of_largest_number_of_upvotes])

print(article_upvotes[article_upvotes.index(max(article_upvotes))])



