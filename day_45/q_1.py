from bs4 import BeautifulSoup

with open("simple.html", encoding='utf-8') as file:
    content = file.read()

soup = BeautifulSoup(content, "html.parser")

print(soup.select("li a"))
