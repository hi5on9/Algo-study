import sys
import heapq
input = sys.stdin.readline
INF = 10000001

N = int(input())
M = int(input())


# computer = [[] for _ in range(N)]
computer = [i for i in range(N)]
num = []

for i in range(M):
    a,b,c = map(int,input().split())
    num.append([a-1,b-1,c])

num = sorted(num,key=lambda x:x[2])
rst = 0

def find(a):
    if computer[a] ==a :
        return a
    computer[a] = find(computer[a])
    return computer[a]

def union(a,b):
    aa = find(a)
    bb = find(b)
    # print(aa,bb)
    if aa==bb: return False #이미 연결쓰 ..
    computer[b] = a
    return True

cnt = 0
# print(num)
for a,b,c in num:
    # if cnt == N-1: break
    aa = find(a)
    bb = find(b)
    if union(aa,bb):
        rst += c
        cnt += 1
        if cnt == N-1:break
    # print(computer)

print(rst)
