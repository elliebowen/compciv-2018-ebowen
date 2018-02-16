from datetime import datetime
from urllib.parse import urljoin
import data_helper
from data_helper import DATA_SRC_URL
from bs4 import BeautifulSoup

def txdate_to_iso(datestr):
    """
    A helper function that, given a date formatted the way that the
    Texas Dept. of Justice does it,
        i.e. MM/DD/YYYY, e.g. '10/24/1988'
        or even: '10/24/88'

    and returns a ISO-formatted string, i.e. YYYY-MM-DD

    Args:
        datestr: a <str>, ostensibly one that is meant to be a
            date value like '10/24/1988'

    Returns:
        <str>: in 'YYYY-MM-DD' format, e.g. '1988-10-24'
    """
    if len(datestr) == 10:
        d = datestr[3:5]
        y = datestr[-4:]
        m = datestr[0:2]
    else:
        m, d, y = datestr.split('/')
        y = '19' + y
    return '-'.join([y,m,d])

def calc_years_diff(start_date, end_date):
    """
    A helper function that, given 2 ISO-formatted date strings
    returns the difference in fractional years, to the nearest 0.1
    of a year.

    Args:
        start_date: <str> the "older" date, in "YYYY-MM-DD" format
        end_date: <str> the "later" date, in "YYYY-MM-DD" format

    Returns:
        <float> A decimal number representing the number of years
           between dates, e.g. 12.4

    Recommendation:
        This is actually quite complicated, thanks to leap years/days/secs, among
        other complications...

        https://stackoverflow.com/questions/4436957/pythonic-difference-between-two-dates-in-years

        Convert the strings into datetime.datetime objects. Then subtract the
          2 objects to get number of days. Divide by that 365 to get the
          estimated years difference. Rounding to the first decimal place
          will be enough precision. And leap years shouldn't make THAT much
          of a difference...
    """


def make_absolute_url(href):
    
    #### fill in yourself
    #### could be a one-liner with proper use of the urljoin() function...
    return urljoin(href, DATA_SRC_URL)
