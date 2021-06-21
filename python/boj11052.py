import sys
import heapq
from collections import deque
import heapq
input = sys.stdin.readline

N = int(input())
cards = list(map(int,input().split()))
dp = [[0 for _ in range(N+1)]for _ in range(N+1)]

cards = [0] + cards

for i in range(N+1):
    for j in range(1,N+1):
        if i > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-i]+cards[i])

# 
# for i in range(N+1):
#     print(dp[i])

print(dp[N][N])


'''
4
1 5 6 7
'''
