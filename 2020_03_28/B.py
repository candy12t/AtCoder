x = int(input())

five_hundred_cnt = 0
five_cnt = 0

if x >= 500:
    five_hundred_cnt = x // 500
    x %= 500
if x >= 5:
    five_cnt = x // 5

print(1000*five_hundred_cnt + 5*five_cnt)
