import urllib.request
from bs4 import BeautifulSoup


class GrabData:
    def __init__(self, site):
        self.site = site

    def getscrape(self):
        r = urllib.request.urlopen(self.site)
        html = r,read()
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)
        for tag in sp.find_all("a"):
            url = tag.get("href")
            print("\n" + url)

getweb = GrabData('https://news.google.com/')
getweb.getscrape()
    
