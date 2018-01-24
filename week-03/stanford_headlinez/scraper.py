import requests

def print_hedz(url='https://wgetsnaps.github.io/stanford-edu-news/news/simple.html'):
    txt = fetch_html(url)
    htags = parse_headline_tags(txt)

    for t in htags:
        hedtxt = extract_headline_text(t)
        print(hedtxt)


def extract_headline_text(txt):
   hedtxt = txt.split('<')
   hedtxt[2].split('<')[0]
                

def parse_headline_tags(txt):
    lines = txt.splitLines()
    list = []
    for line in lines:
        list.append(lines)
    return list    


def fetch_html(url):
    x = requests.get(url)
    txt = x.text
    return txt

 
   