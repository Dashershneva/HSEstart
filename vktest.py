import urllib.request
import json

url = 'https://api.vk.com/method/wall.get?owner_id=-1&count=100'
res = urllib.request.urlopen(url).read().decode('utf-8')

data = json.loads(res)

f = open('vktest.txt', 'w', encoding = 'utf-8')

f.write(res)

print(data)
