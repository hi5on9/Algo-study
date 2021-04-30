import sys
import heapq
input = sys.stdin.readline
INF = 10000001

N,M = map(int,input().split())
dist = []
road = [i for i in range(N)]
def find(a):
    if a == road[a]:
        return a
    road[a] = find(road[a])
    return road[a]

def union(a,b):
    aa = find(a)
    bb = find(b)
    if aa == bb: return False
    road[b] = a
    return True

for _ in range(M):
    a,b,c = map(int,input().split())
    dist.append([a-1,b-1,c])

dist = sorted(dist,key=lambda x:x[2])

rst = 0
cnt = 0
for a,b,c in dist:
    if cnt == N-2 : break
    aa = find(a)
    bb = find(b)
    if union(aa,bb):
        rst += c
        cnt += 1


print(rst)
