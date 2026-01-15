a, b = map(int, input().split())
for n in range(1000000):
    if a * 1000 < b * n:
        print(n)
        break