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
    row = get_and_parse_inmate_rows() 
    for r in row:
        col = r.select('td')
        d['tdcj_id'] = col[0].strip()
        d['url'] = col[1].make_absolute_url.strip()
        d['last_name'] = col[2].strip()
        d['first_name'] = col[3].strip()
        d['birthdate'] = col[4].txtdate_to_iso.strip()
        d['gender'] = col[5].strip()
        d['race'] = col[6].strip()
        d['date_received'] = col[7].txtdate_to_iso.strip()
        d['date_offense'] = col[8].txtdate_to_iso.strip()
        d['age_at_offence'] = int(col[9].strip())
        d['years_before_death_row'] = float(col[10].strip())
    return d
