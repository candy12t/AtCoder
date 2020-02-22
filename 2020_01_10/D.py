import sys

def f(x):
  cnt = 0
  while x%2 == 0:
    x /= 2
    cnt += 1
  return cnt

def gcd(x, y):
  if y:
    return gcd(y, x%y)
  else:
    return x

def lcm(x, y):
  return (x * y) // gcd(x, y)


n, m = map(int, input().split())
a = list(map(int, input().split()))
a = [i//2 for i in a]

t = f(a[0])
for i in range(n):
  if f(a[i]) != t:
    print(0)
    sys.exit()
  a[i] >>= t
m >>= t

l = 1
for i in range(n):
  l = lcm(l, a[i])
  if l > m:
    print(0)
    sys.exit()

m //= l
ans = (m+1) // 2
print(ans)