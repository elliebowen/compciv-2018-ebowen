from data_helper import get_html
from bs4 import BeautifulSoup

def get_and_parse_inmate_rows():
    txt = get_html()
    soup = BeautifulSoup(txt, 'lxml')
    rows = soup.select('tr')
    return rows[1:]

def count_inmates():
    return len(get_and_parse_inmate_rows())