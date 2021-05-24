import sys
input = sys.stdin.readline
MAX_NUM = 10000000

N, M = map(int,input().split())
num = list(map(int,input().split()))
cnt = [0] * M
sss = 0
rst = 0
for i in range(N):
    sss = (sss + num[i]) % M
    # print(sss,end=" ")
    if sss == 0 :
        rst += 1
    cnt[sss] += 1


# print(cnt)
for i in range(len(cnt)):
    # if i == 0: rst += cnt[i]
    rst += ((cnt[i] * (cnt[i]-1))//2)

print(rst)
