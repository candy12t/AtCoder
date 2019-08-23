N, A, B = map(int, input().split())

def digitalSum(n):
  sum = 0
  while n > 0:
    sum += n % 10
    n //= 10
  return sum

total = 0
for i in range(1, N+1):
  sum = digitalSum(i)
  if A <= sum and sum <= B:
    total += i

print(total)