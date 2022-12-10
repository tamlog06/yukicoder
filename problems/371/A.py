N = int(input())

S, C = [], []
for i in range(N):
    s, c = input().split()
    S.append(s)
    C.append(int(c))

num = [0]*8
see = {}
for i in range(N-1, -1, -1):
    if S[i] in see.keys():
        continue

    see[S[i]] = 1
    num[C[i]] += 1

for i in range(8):
    print(num[i])


