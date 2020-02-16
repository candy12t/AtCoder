import itertools

n, k = map(int, input().split())
As = list(map(int, input().split()))
combs = list(itertools.combinations(As, 2))
combs.sort()
print(combs)
multis = []
for comb in combs:
    multi = comb[0] * comb[1]
    multis.append(multi)
multis.sort()
print(multis[k-1])