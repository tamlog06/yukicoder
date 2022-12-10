N, M = map(int, input().split())
from collections import defaultdict
L, R = defaultdict(int), defaultdict(int)

for i in range(M):
    l, r = map(int, input().split())
    L[l] += 1
    R[r-1] += 1

n = 0
for i in range(N, 0, -1):
    n = n + L[i] - R[i]
    print(n)
    

