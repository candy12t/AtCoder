n = int(input())
xs = list(map(int, input().split()))

sum = []
for i in range(1, 101):
    sums = 0
    for x in xs:
        s = (x-i) ** 2
        sums += s
    sum.append(sums)
print(min(sum))
