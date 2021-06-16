import sys
import heapq
from collections import deque
input = sys.stdin.readline

MAX_NUM = 123456789
N,E = map(int,input().split())
graph = [[] for _ in range(N+1)]
v = [MAX_NUM] * (N+1)

ans = [[] for _ in range(N+1)]
q = []
def dij(start,v):
    v[start] = 0
    heapq.heappush(q,(0,start))

    while q:
        ddd , now = heapq.heappop(q)

        if v[now] < ddd:
            continue

        for next_node,w in graph[now]:
            temp = ddd + w
            if temp < v[next_node]:
                v[next_node] = temp
                heapq.heappush(q,(temp,next_node))


for e in range(E):
    a,b,w = map(int,input().split())
    graph[a].append((b,w))
    graph[b].append((a,w))

a,b = map(int,input().split())


v1 = [MAX_NUM] * (N+1)
dij(1,v1)
vA = [MAX_NUM] * (N+1)
dij(a,vA)
vB = [MAX_NUM] * (N+1)
dij(b,vB)

temp1 = v1[a]+vA[b]+vB[N]
temp2 = v1[b]+vB[a]+vA[N]



ans = min(temp1,temp2)
if ans >= MAX_NUM:
    print(-1)
else:print(ans)
