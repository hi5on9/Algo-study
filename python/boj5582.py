import sys,copy
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
from collections import deque
MAX_SIZE = 1234567890


w1 = list(input().rstrip())
w2 = list(input().rstrip())

dp = [[0 for i in range(len(w2)+1)] for j in range(len(w1)+1)]


max_w = 0
for i in range(1,len(w1)+1):
    for j in range(1,len(w2)+1):
        if w1[i-1] == w2[j-1]:
            dp[i][j] = dp[i-1][j-1] +1
            max_w = max(dp[i][j],max_w)


print(max_w)
