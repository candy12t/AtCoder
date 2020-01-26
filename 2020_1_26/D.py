h = int(input())
for i in range(1, 41):
  x = 2 ** i -1
  if h <= x:
    print(x)
    break