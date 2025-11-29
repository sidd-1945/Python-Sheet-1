# l1,r1,l2,r2 = map(int,input().split())
# if l2 >= l1 and r1 <= r2:
#     print(l2,r1)
# elif l2 <= l1 and r1 >= r2:
#     print(l1,r2)
# elif l2 >= l1 and r2 <= r1:
#     print(l2,r2)
# elif l1 >= l2 and r1 <= r2:
#     print(l1,r1)
# else:
#     print("-1") 

l1,r1,l2,r2 = map(int,input().split())
start = max(l1,l2)
end = min(r1,r2)
if start <= end:
    print(start,end)
else:
    print(-1)    
                