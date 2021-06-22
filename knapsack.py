n, weight = map(int, input().split())
w = []
v = []
for i in range(n):
    a,b = map(int,input().split())
    w.append(a)
    v.append(b)

dp = [[0 for i in range(weight+1)] for i in range(n+1)]

for i in range(n):
    for j in range(weight+1):
        if j - w[i] >=0:
            dp[i+1][j] = max(dp[i][j],dp[i][j-w[i]]+v[i])
        else:
            dp[i+1][j] = max(dp[i][j],dp[i][j])
for i in dp:
    print(i)


