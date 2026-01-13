suji = int(input())
line = list(str(suji))
seen = set()
while True:
  if suji in seen:
    print("No")
    break
  else:
    seen.add(suji)
    suji = sum(int(x) ** 2 for x in line)
    line = list(str(suji))
  if suji == 1:
    print("Yes")
    break