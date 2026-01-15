line = sorted(map(int, input().split()))
print("".join(map(str, (line.pop() for _ in range(3)))))