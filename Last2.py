A, B, C, D = map(int, input().split())

result = 1
for x in [A, B, C, D]:
    result = (result * (x % 100)) % 100

print(f"{result:02d}")

