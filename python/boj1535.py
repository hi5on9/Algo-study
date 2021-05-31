import sys
input = sys.stdin.readline
MAX_NUM = 10000001

N = int(input())
minus = list(map(int,input().split()))
plus = list(map(int,input().split()))
minus, plus = [0] + minus, [0] + plus

dp = [[0 for _ in range(101)] for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,101):
        if minus[i] > j :
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - minus[i]] + plus[i])

# for i in range(N):
    # print(dp[i])

print(dp[N][99])
