a,b,c = map(int,input().split())
if a>b:
    if a>c:
        if b<c:
            print(b,a)
        else:
            print(c,a)    
    else:
        print(b,c)  
elif b>c:
    if a<c:
        print(a,b)
    else:
        print(c,b)
else:
    print(a,c)        