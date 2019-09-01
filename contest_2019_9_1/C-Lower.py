import sys
input = sys.stdin.readline
N = int(input())
H = list(map(int, input().split()))
max = 0
for n in range(N):
  count = 0
  for i in range(n,N-1):
    if H[i] >= H[i+1]:
      count += 1
    else:
      break
  if count > max:
    max = count
print(max)