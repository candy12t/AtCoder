import itertools

n, m, q = map(int, input().split())
abcd = [list(map(int, input().split())) for _ in range(q)]

nums = [x for x in range(1, m+1)]
num_list = list(itertools.combinations_with_replacement(nums, n))

result_lst = []
for num in num_list:
    result = 0
    for i in abcd:
        a, b, c, d = i[0], i[1], i[2], i[3]
        x = num[b-1] - num[a-1]
        if x == c:
            result += d
    result_lst.append(result)
print(max(result_lst))
