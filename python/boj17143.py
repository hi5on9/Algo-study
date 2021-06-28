import sys,copy
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
from collections import deque
dy = [0,-1,1,0,0]
dx = [0,0,0,1,-1]

R,C,M = map(int,input().split())
arr = [[0 for _ in range(C+1)] for _ in range(R+1)]
c_arr = [[0 for _ in range(C+1)] for _ in range(R+1)]

shark = [0]
ans = 0
for m in range(M):
    r,c,s,d,z = map(int,input().split())
    shark.append([d,s,z])
    arr[r][c] = (m+1)

def catch_fish(now):
    global ans
    i = 1
    while True:
        if i >= (R+1):
            break
        if arr[i][now] != 0:
            # print("물고기 잡았다!",arr[i][now])
            ans += shark[arr[i][now]][2]
            arr[i][now] = 0
            # print("ans:",ans)
            break
        i+=1
def move(y,x,temp):
    d,speed,size = shark[arr[y][x]]
    now = 0
    ny = y
    nx = x
    while True:
        if now >= speed:
            if not ((1<=ny<=R) and (1<=nx<=C)):
                ny -= dy[d]
                nx -= dx[d]
            if c_arr[ny][nx] != 0:
                temp.append([ny, nx, arr[y][x]])
            else:
                c_arr[ny][nx] = arr[y][x]
            break
        ny += dy[d]
        nx += dx[d]
        now += 1
        if not (1<=ny<=R and 1<=nx<=C):
            if d == 1 or d == 3:
                d += 1
            elif d == 2 or d ==4:
                d -= 1
            shark[arr[y][x]][0] = d
            now -= 2

def eat_shark(temp):
    global arr
    for r,c,idx in temp:
        now_shark = c_arr[r][c]
        # print("---",r,c,idx,c_arr[r][c])
        if shark[now_shark][2] < shark[idx][2]:
            c_arr[r][c] = idx

    arr = copy.deepcopy(c_arr)

def print_shark(arr):
    for i in range(1,R+1):
        for j in range(1,C+1):
            print(arr[i][j],end="  ")
        print()

# print_shark(arr)

for t in range(1,C+1):
    c_arr = [[0 for _ in range(C + 1)] for _ in range(R + 1)]
    catch_fish(t)
    # print_shark(arr)
    temp = []
    for i in range(1,R+1):
        for j in range(1,C+1):
            if arr[i][j] != 0:
                # print(arr[i][j],":",i,j)
                move(i,j,temp)
    # print("이동하고나서,,,")
    # print_shark(c_arr)
    eat_shark(temp)
    # print(temp)
    # print("겹치는거 잡아머금..")
    # print_shark(arr)
    # print("-------")
print(ans)
