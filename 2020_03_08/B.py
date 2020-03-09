a, b, m = map(int, input().split())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

sums = []
for i in range(m):
    m_list = list(map(int, input().split()))
    sum = a_list[m_list[0]-1] + b_list[m_list[1]-1] - m_list[2]
    sums.append(sum)

mins = min(a_list) + min(b_list)
sum_min = min(sums)
print(min(sum_min, mins))
