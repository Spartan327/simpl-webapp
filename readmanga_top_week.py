import requests
import re
from bs4 import BeautifulSoup


def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        print('Сетевая ошибка')
        return False


def get_top5_manga_week():
    url = 'https://readmanga.live'
    html = get_html(url)
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        soup = soup.find(text=re.compile('Популярные на этой неделе'))\
            .find_next('div', class_='row tiles-row short')\
            .find_all('div', class_='simple-tile')
        top5_manga_week = []
        for manga in soup:
            url_manga = url + manga.find('a')['href']
            url_img = manga.find('img')['data-original']
            name_manga = ' '.join(manga.find('div', class_='strong title').text.split())
            top5_manga_week.append({
                'url_manga': url_manga,
                'name_manga': name_manga,
                'url_img': url_img
            })
            print(url_img)
        return top5_manga_week
    return False
