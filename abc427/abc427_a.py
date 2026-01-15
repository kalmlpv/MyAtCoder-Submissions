s = input()
line = list(s)
line[len(s) // 2] = ""
print("".join(line))