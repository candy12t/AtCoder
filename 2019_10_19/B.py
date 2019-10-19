N = int(input())
d_list = list(map(int, input().split()))

sum = 0
for i in range(N):
  for m in range(i+1, N):
    xy = d_list[i]*d_list[m]
    sum += xy

print(sum)