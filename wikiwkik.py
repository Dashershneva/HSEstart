f = open('wiki.txt',encoding='utf-8')
s = f.read()
f.close
a = s.split()
d = {}
for word in a:
    word = word.strip(',.?!:;][1234567890{}()""-_=+<>/')
    word = word.lower()
    if word in d:
        d[word] += 1
    else:
        d[word] = 1
for word in sorted(d):
    print(word,d[word])
