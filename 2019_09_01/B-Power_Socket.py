import math
A, B = map(int, input().split())
n = B - A
count = 1
N = n / (A-1)
count += math.ceil(N)
print(count)