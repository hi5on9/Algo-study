import sys
input = sys.stdin.readline
from collections import deque
from itertools import combinations

N,M = map(int,input().split())
dy = [-1,1,0,0,-1,1,-1,1]
dx = [0,0,-1,1,-1,-1,1,1]
baby_shark = []
ocean = []
safe_dis = [[100 for _ in range(M)] for _ in range(N)]
for i in range(N):
    ocean.append(list(map(int,input().split())))
    for j in range(M):
        if ocean[i][j] == 1:
            baby_shark.append([i,j])
            safe_dis[i][j] = -1

# print(baby_shark)

for y,x in baby_shark:
    v = [[0 for _ in range(M)] for _ in range(N)]
    # print("baby_shark",y,x)
    q = deque()
    q.append([y,x,1])
    while q:
        y , x, dis = q.popleft()
        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < N and 0 <= nx < M and ocean[ny][nx] == 0 and v[ny][nx] == 0:
                v[ny][nx] = 1
                safe_dis[ny][nx] = min(dis,safe_dis[ny][nx])
                q.append([ny,nx,dis+1])
    #
    # for i in range(N):
    #     print(safe_dis[i])

    # print("=========")

ans = 0
for i in range(N):
    for j in range(M):
        ans = max(ans,safe_dis[i][j])

print(ans)
