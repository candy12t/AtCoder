n, k = map(int, input().split())

s = [int(i) for i in range(1, n+1)]

for i in range(k):
    d = int(input())
    as_ = list(map(int, input().split()))

    for a in as_:
        try:
            s.remove(a)
        except ValueError:
            pass
print(len(s))
