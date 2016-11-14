f = open('C:\\Users\\student\\Desktop\\new.txt','w',encoding='utf-8')
l = ''
s = ''
while (s != 'хватит'):
    s = input('введите слово')
    f.write(s)
f.close()
    
