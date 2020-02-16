import collections

n = int(input())
s = [input() for _ in range(n)]
cnt = collections.Counter(s)

values, cnts = zip(*cnt.most_common())
maxCnt = cnts[0]
maxStr = []
for i in range(len(cnts)):
    if cnts[i] == maxCnt:
        maxStr.append(values[i])
maxStr.sort()
for i in maxStr:
    print(i)