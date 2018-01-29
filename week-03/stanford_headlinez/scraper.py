import requests

def print_hedz(url='https://wgetsnaps.github.io/stanford-edu-news/news/simple.html'):
    txt = fetch_html(url)
    htags = parse_headline_tags(txt)

    for t in htags:
        hedtxt = extract_headline_text(t)
        print(hedtxt)


def extract_headline_text(txt):
   headlist = txt.split('>')
   headtxt = headlist[2]
   frags = headtxt.split('<')
   headline = frags[0]
   return headline 
                

def parse_headline_tags(txt):
    lines = txt.splitlines()
    headline_list = []
    for line in lines:
        if '<h3><a' in line: 
            headline_list.append(line)
    return headline_list    


def fetch_html(url):
    x = requests.get(url)
    txt = x.text
    return txt

 
   