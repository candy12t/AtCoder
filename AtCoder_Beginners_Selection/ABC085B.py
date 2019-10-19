N = int(input())
dlist = [int(input()) for i in range(N)]

dlist.sort(reverse=True)
max = dlist[0]
count = 1

for d in dlist:
  if max > d:
    max = d
    count += 1
print(count)

# print(len({input()for _ in range(int(input()))}))