a, b, n = map(int, input().split())

y = n//b
if y == 0:
    x = n
else:
    x = b - 1
print(int(a*x/b) - a*int(x/b))
