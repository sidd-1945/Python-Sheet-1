# a,b,c,d = map(int,input().split())
# ans = float ((a*b*c*d)/100)
# ans2=str(ans).split(".")[1]
# print(ans2)

a,b,c,d = map(int,input().split())
mul = (a*b*c*d)%100
print(f"{mul}:02d")