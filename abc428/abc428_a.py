speed, runtime, stoptime, giventime = map(int, input().split())
kyori = 0
kaisu = giventime // (runtime + stoptime)
kyori += speed * runtime * kaisu
amari = giventime % (runtime + stoptime)
if amari < runtime:
    kyori += amari * speed
else:
    kyori += runtime * speed
print(kyori)