import itertools # 順列生成
N = int(input())
P_list = tuple(map(int, input().split()))
Q_list = tuple(map(int, input().split()))
raw = list(itertools.permutations(range(1, N+1)))
print(abs(raw.index(P_list) - raw.index(Q_list)))