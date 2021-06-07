import sys
input = sys.stdin.readline
from collections import deque
MAX_NUM = 10000001
dy = [-1,1,0,0]
dx = [0,0,-1,1]

N = int(input())
seat = [[0 for _ in range(N+1)] for _ in range(N+1)]
loc = [[0,0,0,0] for _ in range(N*N+1)]  # 친한친구 , 빈칸 , 위치
best_friend = [0] * (N*N+1)
last_seat = [0,0]
# print(loc)

def check(a,b,c,d):
    global last_seat
    fav_friend = [a,b,c,d]
    for i in range(N):
        for j in range(N):
            if seat[i][j] == 0:
                loc.append([0, 0, i, j])
                idx = len(loc) - 1
                for k in range(4):
                    ny = i + dy[k]
                    nx = j + dx[k]
                    if 0<= ny <N and 0<=nx<N :
                        if seat[ny][nx] in fav_friend:
                            loc[idx][0] += 1
                        elif seat[ny][nx] == 0:
                            loc[idx][1] += 1
            if i == j == (N-1):
                last_seat = [i,j]
            # else:
            #     print("못 앉는 자리 !!",i,j)


for n in range(N*N):
    X, a,b,c,d = map(int,input().split())
    best_friend[X] = [a,b,c,d]
    loc = []
    check(a,b,c,d)
    if len(loc) != 0:
        loc = sorted(loc,key=lambda x:(x[0],x[1]),reverse=True)
        # print(loc)
        y,x  = loc[0][2],loc[0][3]
    else :
        y,x = last_seat[0], last_seat[1]
    seat[y][x] = X

    # for i in range(N+1):
    #     print(seat[i])
    # print("=============")

# print(best_friend)
ans = 0
for i in range(N):
    for j in range(N):
        cnt = 0
        for k in range(4):
            ny = i + dy[k]
            nx = j + dx[k]
            if 0 <= ny < N and 0 <= nx < N:
                if seat[ny][nx] in best_friend[seat[i][j]]:
                    cnt += 1

        if cnt == 1 :ans +=1
        elif cnt == 2 : ans += 10
        elif cnt == 3 : ans +=100
        elif cnt == 4:ans += 1000

print(ans)
