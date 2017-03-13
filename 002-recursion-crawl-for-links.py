import requests
from BeautifulSoup import BeautifulSoup


def iterrative_crawl(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text)
    c = []
    for link in soup.findAll('a'):
        url = link.get('href')
        if url.startswith("http") and url not in c:
            c.append(url)
            print c

iterrative_crawl("https://www.grammarly.com")