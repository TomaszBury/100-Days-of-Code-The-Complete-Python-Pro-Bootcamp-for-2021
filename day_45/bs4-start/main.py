from bs4 import BeautifulSoup

with open("website.html", encoding='utf-8') as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
print(soup.title)
print(soup.title.name)
print(soup.title.string)

print(soup)

print(soup.prettify())

print("\n")
print(soup.a)

print("\n")

print(soup.li.string)
print(soup.li)
print("\n")
print(soup.findAll(name="a"))

all_anchor_tags = soup.find_all(name="a")
for tag in all_anchor_tags:
    #print(tag.getText())
    print(tag.get("href"))


heading = soup.find(name="h1", id="name")
print(heading.string)


section_heading = soup.find(name="h3", class_="heading")
print(section_heading.getText())
print(section_heading.name)
print(section_heading.get("class"))

