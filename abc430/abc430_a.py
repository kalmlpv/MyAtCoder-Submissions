amelimit, cookieneeded, ame, cookie = map(int, input().split())
if ame < amelimit:
    print("No")
else:
    if cookie < cookieneeded:
        print("Yes")
    else:
        print("No")