a = int(input())
year = a//365
b = a-365*year
month = b//30
days = b%30
print(year,"years")
print(month,"months")
print(days,"days")