from collections import deque

INF = 1001001001
di = (-1, 0, 1, 0)
dj = (0, -1, 0, 1)

h, w = map(int, input().split())
s = [input() for _ in range(h)]
ans = 0

for si in range(h):
  for sj in range(w):
    if s[si][sj] == '#':
      continue
    dist = [[INF] * w for _ in range(h)]
    dist[si][sj] = 0
    q = deque([(si, sj)])
    while q:
      i, j = q.popleft()
      for dir in range(4):
        ni = i + di[dir]
        nj = j + dj[dir]
        if (ni<0 or ni>=h or nj<0 or nj>=w):
          continue
        if s[ni][nj] == '#':
          continue
        if dist[ni][nj] != INF:
          continue
        q.append((ni, nj))
        dist[ni][nj] = dist[i][j]+1
    for i in range(h):
      for j in range(w):
        if dist[i][j] == INF:
          continue
        ans = max(ans, dist[i][j])
print(ans)