import requests
from bs4 import BeautifulSoup

pages = ['https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc', 'https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc&start=51&ref_=adv_nxt']

for links in pages:
    movie_titles = []
    movie_numbers = []
    movie_links = []

    response = requests.get(links)
    html_file = response.text
    soup = BeautifulSoup(html_file, "html.parser")

    movies_content = soup.findAll("h3", class_="lister-item-header")
    for movies in movies_content:
        movie_titles.append(movies.find('a').getText())
        movie_numbers.append(movies.find('span', class_="lister-item-index unbold text-primary").getText())
        movie_links.append(movies.find('a').get('href'))

    with open(file="movies.txt", mode='a') as file:
        for i in range(0, len(movie_numbers)):
            file.write(f"{movie_numbers[i]}) {movie_titles[i]}, trailer: https://www.imdb.com{movie_links[i]}\n")
