N, M = map(int, input().split())
D = list(list(map(int, input().split())) for _ in range(N))
for i in range(N):
    D[i].sort()

import bisect
ans = float('inf')

for i in range(M):
    tmp = -1
    flag = False
    A = D[0][i]
    for j in range(1, N):
        idx = bisect.bisect_left(D[j], A)
        if idx == M:
            flag = True
            break

        tmp = max(tmp, D[j][idx]-A)
        A = D[j][idx]

    if flag:
        break
    ans = min(ans, tmp)

if ans == float('inf'):
    print(-1)
else:
    print(ans)
