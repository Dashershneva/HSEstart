import re
import random

def newtext():
    z = random.chioce()
    f = open('C:\\Users\\student\\Desktop\\tolstoy.txt','r',encoding='utf-8')
    s = f.read()
    a = s.split(' ')
    d = {}
    reg = '(л[аи]?$)'

    for word in a:
        word = word.strip(':;?!.,"')
        if re.search(reg,word):
            d[word] = 'глагол'
        else:
            d[word] = 1

    return z
