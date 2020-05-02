x = int(input())

a = 1.01
m = 100
cnt = 0

while m < x:
    m = int(m) * a
    cnt += 1
print(cnt)