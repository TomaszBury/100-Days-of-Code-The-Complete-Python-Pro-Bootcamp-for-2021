from bs4 import BeautifulSoup

with open("maxlength.html", encoding='utf-8') as file:
    content = file.read()

soup = BeautifulSoup(content, "html.parser")

form_tag = soup.find("input")
print(form_tag.get("maxlength"))
