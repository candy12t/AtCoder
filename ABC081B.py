N = int(input())
A = list(map(int, input().split()))

count = 0
while True:
  odd = False
  for n in range(N):
    if A[n] % 2 != 0:
      odd = True
  if odd:
    break
  for n in range(N):
    A[n] /= 2
  count += 1
print(count)