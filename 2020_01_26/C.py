n, k = map(int, input().split())
h = list(map(int, input().split()))

h.sort(reverse=True)
del h[:k]
cnt = sum(h)
print(cnt)