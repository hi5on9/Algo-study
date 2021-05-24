import sys
input = sys.stdin.readline
MAX_NUM = 10000000

N, H = map(int,input().split())
down = [0] * (H+1)
up = [0] * (H+1)

for n in range(N):
    M = int(input())
    if n % 2 == 0:
        down[M] += 1
    else :
        up[M] += 1

for i in range(H-1,0,-1):
    down[i] += down[i+1]
    up[i] += up[i+1]

# print(down)
# print(up)

min_cnt = n
range_cnt = 0
for i in range(1,H+1):
    # print(min_cnt,down[i],up[H-i+1])
    if min_cnt > (down[i] + up[H-i+1]):
        min_cnt = (down[i] + up[H-i+1])
        range_cnt = 1
    elif min_cnt == (down[i] + up[H-i+1]):
        range_cnt += 1

print(min_cnt,range_cnt)

