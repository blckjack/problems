
import re
import requests
from BeautifulSoup import BeautifulSoup
"""
from urllib2 import HTTPError


collect = []
def recursive_crawl(url, depth=1):
    if depth == 0: return
    try:
        #response = urllib2.urlopen(url)
    except HTTPError as e:
        raise

    match = re.findall(r'(https://.+)".*', response.read())
    if match and match not in collect:
        collect.extend(match)

    for item in collect:
        if requests.get(item):
            recursive_crawl(url, depth-1)
recursive_crawl("https://www.vk.com")
print collect
"""

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