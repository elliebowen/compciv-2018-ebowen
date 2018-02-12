import requests
from bs4 import BeautifulSoup

OFFICIAL_URL='https://www.stanford.edu/news/'
SAMPLE_URL = 'https://wgetsnaps.github.io/stanford-edu-news/news/simple.html'

def fetch_hedz(url=OFFICIAL_URL):
    txt = fetch_html(url)
    tags = parse_headline_tags(txt)
    headlines = []
    for x in tags:
        result = extract_headline_data(x)
        headlines.append(result)
    return headlines

def extract_headline_data(tag):
    return {'url': tag.attrs['href'], 'title': tag.text}

def fetch_html(url):
    x = requests.get(url)
    return x.text

def parse_headline_tags(txt):
    soup = BeautifulSoup(txt, 'lxml')
    return soup.select('h3 a')

def print_hedz(url=OFFICIAL_URL):
    headlines = fetch_hedz(url)
    for hed in headlines:
        print(hed['title'])