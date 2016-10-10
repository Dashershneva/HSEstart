a = input('enter your word')
if a.endswith('а'):
    print('1st female')
elif a.endswith('о' or 'е'):
    print('2nd neutral')
elif a.endswith('ь'):
    print('3rd female')
else:
    print('2nd male')
    
