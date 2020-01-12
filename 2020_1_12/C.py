n, m = map(int, input().split())
sp = [[i for i in input().split()] for _ in range(m)]

ac = 0
wa = 0
for i in range(m):
  s = sp[i][0]
  p = sp[i][1]
  if p == 'AC':
    ac += 1
  else:
    wa += 1
  
print(ac, wa)