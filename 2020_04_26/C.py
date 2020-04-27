n = int(input())
s = [input() for _ in range(n)]

cnt = len(set(s))
if cnt <= n:
    print(cnt)
else:
    print(n)
