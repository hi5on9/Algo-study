import sys
input = sys.stdin.readline
from collections import deque
dy = [-1,1,0,0]
dx = [0,0,-1,1]

M,N= map(int,input().split())
arr = []
v = [[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
    arr.append(list(input().rstrip()))

q = deque()
q.append([0,0,0,0]) # y,x,cnt,wall
v[0][0] = 1

ans = []
while q:
    y,x,cnt,wall = q.popleft()
    # print(y,x,":",cnt,wall)
    if y == N-1 and x == M-1:
        ans.append(wall)
        # print(cnt,wall)
        break
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0<=ny<N and 0<=nx<M and v[ny][nx] ==0:
            if arr[ny][nx] == '1':
                q.append([ny,nx,cnt+1,wall+1])
            else:
                q.appendleft([ny,nx,cnt+1,wall])
            v[ny][nx] = 1

# print(ans)
print(min(ans))
