f = open('C:\\Users\\student\\Desktop\\new.txt','w',encoding='utf-8')
a = ''
line = ''
while (a != 'хватит'):
    a = input('введите слово')
    line += a
    print(len(a))
    s = list(a)
    b = ''.join(s[-1::-1])
    if a == b:
        line += ' ' 'yes' + ' '
        print('yes')
    else:
        line += ' ' 'no' + ' '
        print('no')
    if a.endswith(('аю', 'у', 'ю', 'ешь', 'ишь', 'ет', 'ит', 'ем', 'им', 'ете', 'ите', 'ют', 'ят')):
        line += 'глагол' + ' \n'
        print('глагол')
    else:
        line += '\n'
f.write(line)
f.close()
