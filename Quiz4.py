import requests
from bs4 import BeautifulSoup
from time import sleep
import csv
from random import randint

h = {'Accept-language': 'en-UD'}

file = open('movies.csv', 'w', newline='\n', encoding="utf-8")
f_obj = csv.writer(file)
f_obj.writerow(['Title', 'Year', 'Rating', 'IMG_URL'])
page = 1
while page <= 5:
    url = 'https://movie.ge/filter-movies?type=movie&page=' + str(page)
    r = requests.get(url, headers=h)
    soup = BeautifulSoup(r.text, 'html.parser')
    sub_soup = soup.find('div', class_='mlist section')
    movies_wrapper = sub_soup.findAll('div', class_='popular-card')
    for each in movies_wrapper:
        img_url = each.div.img.attrs.get('data-src')
        # print(img_url)
        title_wrapper = each.find('div', class_='popular-card__title')
        # print(title_wrapper)
        title = title_wrapper.h2.a.span.text
        rating = each.div.find('div', class_='imdb').span.text
        year = each.div.find('div', class_='year').text
        year = year.replace('წ', '').strip()
        print(year)
        f_obj.writerow([title, year, rating, img_url])
    page += 1
    sleep(randint(15, 20))
