import sys
input = sys.stdin.readline
from collections import deque
MAX_NUM = 123456789
dy = [-1,1,0,0]
dx = [0,0,-1,1]
# 북 남 서 동
'''
남동, 서북, 북서, 동남 , 13,02
동북, 남서,  ,03,12
'''
H,W = map(int,input().split())
v = [[MAX_NUM for _ in range(H)] for _ in range(W)]
arr = []


c_loc = []
for w in range(W):
    arr.append(list(input().rstrip()))
    for index, a in enumerate(arr[w]):
        if a =='C' : c_loc.append([w,index])



y,x = c_loc[0][0],c_loc[0][1]
gy, gx = c_loc[1][0],c_loc[1][1]

ans = MAX_NUM
def find(y,x,a):
    global ans
    q = deque()
    q.append([y,x,0,a])
    v[y][x] = 0
    while q:
        y,x,cnt,dir = q.popleft()
        # print(y,x,cnt,dir)
        if y == gy and x == gx:
            # print(gy,gx,cnt)
            ans = min(cnt,ans)

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if not (0<=ny<W and 0<=nx<H):continue
            if arr[ny][nx]=='*':continue
            temp = cnt
            if dir != i: temp += 1
            if v[ny][nx] < temp: continue

            v[ny][nx] = temp
            q.append([ny,nx,temp,i])

    # for i in range(W):
    #     print(v[i])


find(y,x,0)
find(y,x,1)
find(y,x,2)
find(y,x,3)

print(ans)
