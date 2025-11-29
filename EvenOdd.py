a = int(input())
while a > 0:
    if a >= 10:
        a = int(a/10)
    else:
        if a%2==0:
            print("EVEN")
            break
        else:
            print("ODD")
            break