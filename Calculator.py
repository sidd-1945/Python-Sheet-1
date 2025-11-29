a = input()
if '+' in a:
    c,d = a.split('+')
    print(int(c) + int(d))
elif '-' in a:
    c,d = a.split('-')
    print(int(c) - int(d))    
elif '*' in a:
    c,d = a.split('*')
    print(int(c) * int(d))
else:
    c,d = a.split('/')
    print(int(c) // int(d))