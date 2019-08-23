N, Y = map(int, input().split())

bill10000 = -1
bill5000 = -1
bill1000 = -1

for a in range(N+1):
  for b in range(N+1-a):
    c = N - a - b
    total = 10000*a + 5000*b + 1000*c
    if total == Y:
      bill10000 = a
      bill5000 = b
      bill1000 = c

print(bill10000, bill5000, bill1000)