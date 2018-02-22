from bs4 import BeautifulSoup
import data_helper
from format_helper import calc_years_diff
from format_helper import make_absolute_url
from format_helper import txdate_to_iso
from data_helper import get_html


def get_inmate_data():
    inmaterows = get_and_parse_inmate_rows()
    the_data = []
    for row in inmaterows:
        d = wrangle_inmate_data_from_tag(row)
        the_data.append(d)
    return the_data


def get_and_parse_inmate_rows():
    soup = BeautifulSoup(get_html(), 'lxml')
    rows = soup.select('tr')
    return rows[1:]



def wrangle_inmate_data_from_tag(rowtag):
    d = {}
    col = rowtag.select('td')
    d['tdcj_id'] = col[0].text.strip()
    d['url'] = make_absolute_url( col[1].select('a')[0].attrs['href']) 
    d['last_name'] = col[2].text.strip()
    d['first_name'] = col[3].text.strip()
    d['birthdate'] = txdate_to_iso(col[4].text.strip())
    d['gender'] = col[5].text.strip()
    d['race'] = col[6].text.strip()
    d['date_received'] = txdate_to_iso(col[7].text.strip())
    d['date_offense'] = txdate_to_iso(col[8].text.strip())
    d['age_at_offence'] = col[9].text
    d['years_before_death_row'] = col[10].text
    return d
