import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

# Response will get the html code from URL
respons = requests.get(URL)

soup = BeautifulSoup(respons.text, "html.parser")

movies = soup.find_all(name="h3", class_="title")
movie_list = []
for movie in movies:
    top_movie = movie.get_text()
    movie_list.append(top_movie)

with open("movie.txt", "w", encoding="utf-8") as file:
    for item in list(reversed(movie_list)):
        file.write(f"{item}\n")
