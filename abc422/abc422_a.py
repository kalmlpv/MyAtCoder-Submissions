place = input()
line = list(place)
w = int(line[0])
s = int(line[2])

if w == 8:
    s += 1
else:
    if s == 8:
        w += 1
        s = 1
    else:
        s += 1

print(str(w) + "-" + str(s))
