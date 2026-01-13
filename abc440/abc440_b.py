hiki = int(input())
timetable = list(map(int, input().split()))
sorttable = sorted(timetable)
print(timetable.index(sorttable[0]) + 1,timetable.index(sorttable[1]) + 1,timetable.index(sorttable[2]) + 1)