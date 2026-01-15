sx, sy = input().split()
o = "Ocelot"
s = "Serval"
l = "Lynx"

if sx == o:
    x = 1
elif sx == s:
    x = 2
else:
    x = 3

if sy == o:
    y = 1
elif sy == s:
    y = 2
else:
    y = 3

print("Yes" if x - y >= 0 else "No")