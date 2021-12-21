from bs4 import BeautifulSoup
import requests

YYYY_MM_DD = input("Travel to YYYY-MM_DD: ")
print(f"What it is here: {YYYY_MM_DD}")

url_billboard = "https://www.billboard.com/charts/hot-100/" + YYYY_MM_DD + "/"

response = requests.get(url_billboard)

billboard_web_page = response.text
soup = BeautifulSoup(billboard_web_page, "html.parser")

list_of_songs = soup.find_all("span", class_="c-label")
song_names = [song.getText() for song in list_of_songs]

new_song_names = []
new_song_name = ""
for song in song_names:
    for char in song:
        if char != "\n":
            new_song_name += char
    new_song_names.append(new_song_name)
    new_song_name = ""

print(new_song_names)
list_billboard = []
for song in new_song_names:
    try:
        n = int(song)
    except ValueError:
        list_billboard.append(song)

new_song_names = []
for song in list_billboard:
    if song != '-' and song != "NEW":
        new_song_names.append(song)

print(new_song_names)
print(f"Number in the list: {len(new_song_names)}")




