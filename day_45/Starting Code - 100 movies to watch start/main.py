import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
all_movies = soup.findAll(name="h3", class_="title")
movie_titles = [movie.getText() for movie in all_movies]
# movie_titles = [movie.getText().split(" ")[1:] for movie in all_movies]
# print(movie_titles[::-1])
movies = movie_titles[::-1]
# movie_title = []
# for movie in movie_titles:
#     title = ""
#     for text in movie:
#         # print(movie.index(text))
#         if movie.index(text) < len(movie)-1:
#             title += text + " "
#         else:
#             title += text
#     movie_title.append(title)
#
# print((movie_title[::-1]))

with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie} \n")

