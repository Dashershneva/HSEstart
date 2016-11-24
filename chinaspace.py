import re
f = open('chinaspace.txt',encoding='utf-8')
s = f.read()
words = s.split(' ')
reg = '(«[А-Я].+?»)'
for word in words:
    if re.search(reg,word):
        print(word)

