import re
r = '[аоуыиэеыё]'
f = open('C:\\Users\\student\\Desktop\\text1.txt', encoding='utf-8')
s = f.read()
words = s.split(' ')
a = re.findall(r,s)
print(len(a))
