n, a, b = map(int, input().split())

MOD = 10**9 + 7
x = 1
y = 1
ans = pow(2, n, MOD) - 1

for i in range(1, b+1):
    x = x * i % MOD
    y = y * (n-i+1) % MOD
    if i == a or i == b:
        ans -= y * pow(x, MOD-2, MOD)

print(ans%MOD)