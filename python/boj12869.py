import sys
input = sys.stdin.readline
from collections import deque
MAX_NUM = 10000001
dp = [[[-1 for _ in range(61)]for _ in range(61)]for _ in range(61)]
'''
1atk => hp -9
2atk => hp -3
3atk => hp -1

hp < 0 => scv 파괴
한번의 공격에서 같은 scv 여러번 공격 x
'''

def attack(a,b,c):
    if a < 0 : return attack(0,b,c)
    if b < 0 : return attack(a,0,c)
    if c < 0 : return attack(a,b,0)


    if a ==0 and b == 0 and c == 0:
        return 0

    if dp[a][b][c] != -1:
        return dp[a][b][c]

    dp[a][b][c] = MAX_NUM
    dp[a][b][c] = min(dp[a][b][c],attack(a-9,b-3,c-1)+1)
    dp[a][b][c] = min(dp[a][b][c],attack(a-9,b-1,c-3)+1)
    dp[a][b][c] = min(dp[a][b][c],attack(a-3,b-9,c-1)+1)
    dp[a][b][c] = min(dp[a][b][c],attack(a-3,b-1,c-9)+1)
    dp[a][b][c] = min(dp[a][b][c],attack(a-1,b-3,c-9)+1)
    dp[a][b][c] = min(dp[a][b][c],attack(a-1,b-9,c-3)+1)


    return dp[a][b][c]


N = int(input())
arr = list(map(int,input().split()))

scv = [-1] * 3

for idx, a in enumerate(arr):
    scv[idx] = a

ans = attack(scv[0],scv[1],scv[2])
print(ans)
