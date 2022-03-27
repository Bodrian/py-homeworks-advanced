import requests
from bs4 import BeautifulSoup
import re
import task1

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:98.0) Gecko/20100101 Firefox/98.0',
    'Accept-Language': 'en-US,en;q=0.5',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'cross-site',
}

url = 'https://habr.com/ru/all/'

KEYWORDS = ['костей', 'Кластер хранения', 'web', 'python', 'понимание']

@task1.decor_log
def task(KEYWORDS, url, HEADERS):
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, features='html.parser')
    articles = soup.find_all(class_='tm-article-snippet')
    for article in articles:
        for key in KEYWORDS:
            article_text = article.find_all(string=re.compile(key))
            if len(article_text) != 0:
                time = article.find(class_='tm-article-snippet__datetime-published').find('time')['title']
                title = article.find(class_='tm-article-snippet__title-link').text
                link =  article.find(class_='tm-article-snippet__title-link')['href']
                print(f'Статья: {time} - {title} - {url + link}')



if __name__ == "__main__":
    task(KEYWORDS, url, HEADERS)