import sys,copy
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
from collections import deque
dy = [-1,1,0,0]
dx = [0,0,-1,1]

N,K = map(int,input().split())
jump = list(input().rstrip())
num = [0]
size = 0
n = 1
for i in range(N*2-1):
    num.append(n)
    if i >=N:
        size -= 1
    else:
        size += 1
    n += size

# print(num)

ans = 1
y,x = 1,1
for j in jump:
    idx = -1
    if j == 'U':idx = 0
    elif j == 'D':idx = 1
    elif j =='L':idx=2
    elif j =='R':idx=3

    y = y + dy[idx]
    x = x + dx[idx]

    line = y+x -1
    # print(y,x,line)
    temp = 0
    if line <= N:
        if line % 2 == 0:
            temp = num[line] + (y-1)
        else:
            temp = num[line] + (x-1)
    else:
        if line % 2 == 0:
            temp = num[line] + (N-x)
        else:
            temp = num[line] + (N-y)
    # print(temp)
    ans += temp

print(ans)
