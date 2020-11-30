from requests import get
from bs4 import BeautifulSoup
import os

def get_all_blogs():
    urls = ['https://codeup.com/codeups-data-science-career-accelerator-is-here/', 
            'https://codeup.com/data-science-myths/',
            'https://codeup.com/data-science-vs-data-analytics-whats-the-difference/',
            'https://codeup.com/10-tips-to-crush-it-at-the-sa-tech-job-fair/',
            'https://codeup.com/competitor-bootcamps-are-closing-is-the-model-in-danger/']
    l = []
    for url in urls:
        d = {}
        headers = {'User-Agent': 'Codeup Data Science'}
        response = get(url, headers=headers)
        soup = BeautifulSoup(response.text, features='lxml')
        article = soup.find('div', class_='jupiterx-post-content')
        title = soup.find('h1').text
        d['title'] = title
        d['article'] = article.text
        l.append(d)
    return l


def get_all_news():
    urls = ['https://inshorts.com/en/read/sports', 'https://inshorts.com/en/read/business',
        'https://inshorts.com/en/read/technology', 'https://inshorts.com/en/read/entertainment']
    l = []
    for url in urls:
        response = get(url)
        soup = BeautifulSoup(response.text, features='lxml')
        cards = soup.find_all('div', class_='news-card')
        for card in cards:
            d = {}
            title = (card.find('span', itemprop='headline').text)
            article = (card.find('div', itemprop='articleBody').text)
            d['title'] = title
            d['aritcle'] = article
            d['category'] = url.split('/')[-1]
            l.append(d)
    return l