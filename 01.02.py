import urllib.request
import lxml.html

html = urllib.request.urlopen('http://www.kommersant.ru/doc/3207074').read()
f = open('kommersant.html', 'w', encoding='utf-8')
f.write('html')
print(html)
