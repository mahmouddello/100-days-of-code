import requests
from bs4 import BeautifulSoup

link = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(link)

soup = BeautifulSoup(response.text, 'html.parser')

titles = soup.findAll(name='h3', class_='title')

titles = [title.get_text().replace(":", ")").split(")") for title in titles]

movie_titles = [titles[i][1].removeprefix(" ") for i in range(len(titles))]
movie_rankings = [titles[i][0] for i in range(len(titles))]

# Reversing the lists
movie_titles = movie_titles[::-1]
movie_rankings = movie_rankings[::-1]

with open("movies.txt", 'w', encoding="utf-8") as file:
    for i in range(len(movie_titles)):
        file.write(f"{movie_rankings[i]}) {movie_titles[i]}\n")
