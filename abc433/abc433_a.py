takahashi, aoki, bai = map(int, input().split())
bigger = max(takahashi, aoki)
flag = 0
for i in range(100):
    if takahashi + i == (aoki + i) * bai:
        flag = 1
        break

if flag == 0:
    print("No")
else:
    print("Yes")