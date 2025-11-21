import math
a,b = map(int,input().split())
k = a/b
f = math.floor(k)
c = math.ceil(k)
r = math.floor(k + 0.5)
print("floor",a,"/",b,"=",f)
print("ceil",a,"/",b,"=",c)
print("round",a,"/",b,"=",r)