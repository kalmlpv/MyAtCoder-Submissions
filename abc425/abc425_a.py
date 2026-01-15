n = int(input())
sigma = 0
for k in range(n):
    i = k + 1
    if i % 2 == 0:
        sigma += i ** 3
    else:
        sigma -= i ** 3

print(sigma)