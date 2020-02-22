import math

def f(x, y):
    return math.factorial(x) // (math.factorial(x - y) * math.factorial(y))

n, a, b = map(int, input().split())

sum = 0
for i in range(n//2):
    x = f(n, i+1)
    sum += x
ans = sum*2+1

if n%2 == 0:
    ans = sum*2+1-x
ans = ans - f(n, a) - f(n, b)
ans %= ((10**9)+7)
print(ans)