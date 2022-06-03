import sys,copy
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
from collections import deque

N, M = map(int, input().split())
room = [list(input().rstrip()) for _ in range(N)]
v = [[0] * M for _ in range(N)]

dir = [-1,1]

def dfs(y, x , shape, cnt):
    if shape == '|':
        for i in range(2):
            ny = y + dir[i]
            if 0 <= ny < N  and room[ny][x] == shape and v[ny][x] == 0:
                v[ny][x] = cnt
                dfs(ny,x,shape,cnt)
    if shape == '-':
        for i in range(2):
            nx = x + dir[i]
            if 0 <= nx < M  and room[y][nx] == shape and v[y][nx] == 0:
                v[y][nx] = cnt
                dfs(y,nx,shape,cnt)


cnt = 0
for n in range(N):
    for m in range(M):
        if v[n][m] == 0:
            cnt += 1
            dfs(n,m,room[n][m],cnt)

print(cnt)


