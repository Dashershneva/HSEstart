import urllib.request
from bs4 import BeautifulSoup

resp = urllib.request.urlopen('http://www.bbc.com/news')
html = resp.read().decode("utf-8")
resp.close()

f = open("bbc.html", 'w')
f.write(html)

with open("bbc.html") as output_file:
    output_file.write(r.text.encode('utf-8'))
