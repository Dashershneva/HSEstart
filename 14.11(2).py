f = open('C:\\Users\\student\\Desktop\\new.txt','w',encoding='utf-8')
a = ''
while (a != 'хватит'):
    a = input('введите слово')
    print(len(a))
    s = list(a)
    b = ''.join(s[-1::-1])
    if a == b:
        print('yes')
    else:
        print('no')
f.write(a)
f.close()
