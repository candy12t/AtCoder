s = input()

x = 2019
n = len(s)
cnt = 0

for i in range(n):
    for j in range(i+1, n+1):
        if int(s[i:j]) % x == 0:
            cnt += 1
print(cnt)