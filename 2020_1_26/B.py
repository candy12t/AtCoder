h, n = map(int, input().split())
a = list(map(int, input().split()))
for x in a:
  h -= x
if h > 0:
  print('No')
else:
  print('Yes')