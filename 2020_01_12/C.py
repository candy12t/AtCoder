n, m = map(int, input().split())

ac = [False] * n
pena = [0] * n

acCnt = 0
waCnt = 0
for i in range(m):
  p, s = input().split()
  p = int(p) - 1
  if ac[p]:
    continue
  if s == 'AC':
    ac[p] = True
    acCnt += 1
    waCnt += pena[p]
  else:
    pena[p] += 1

print(acCnt, waCnt)