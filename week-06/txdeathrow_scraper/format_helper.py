from datetime import datetime
from urllib.parse import urljoin
import data_helper
from data_helper import DATA_SRC_URL
from bs4 import BeautifulSoup

def txdate_to_iso(datestr):
    m, d, y = datestr.split('/')
    if len(y) == 2:
       y = '19' + y
    return '-'.join([y,m,d])

def calc_years_diff(start_date, end_date):
    date_start = datetime.strptime(start_date, '%Y-%m-%d')
    date_end = datetime.strptime(end_date, '%Y-%m-%d')
    return round((date_end - date_start).days / 365, 1)
 
def make_absolute_url(href):
    return urljoin(data_helper.DATA_SRC_URL, href)
