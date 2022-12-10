N, M, L = map(int, input().split())
A = list(map(int, input().split()))

dp = [[False]*(1001) for _ in range(N+1)]
dp[0][L] = True

for i in range(N):
    for j in range(1001):
        if dp[i][j]:
            dp[i+1][j] = True
            dp[i+1][(j+A[i])//2] = True

if dp[N][M]:
    print("Yes")
else:
    print("No")
