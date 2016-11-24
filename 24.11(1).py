import re
reg = '(б[аоуыиэеыё])'
f = open('C:\\Users\\student\\Desktop\\text1.txt', encoding='utf-8')
s = f.read()
words = s.split(' ')
for word in words:
    if re.search(reg,word):
        res = re.search(reg,word)
        print(res.group(1))
