import sys
import heapq
from collections import deque
input = sys.stdin.readline


N,M = map(int,input().split())
indegree = [0] * N
graph = [[] for i in range(N)]
for _ in range(M):
    a,b = map(int,input().split())
    indegree[b-1] +=1
    graph[a-1].append(b-1)

# print(indegree)
# print(graph)

q = []

for i in range(N):
    if indegree[i] == 0:
        heapq.heappush(q,i)

answer = []
while q:
    idx = heapq.heappop(q)
    answer.append(idx)
    books = graph[idx]

    for b in books:
        if indegree[b] != 0:
            indegree[b] -= 1
        if indegree[b] == 0:
            heapq.heappush(q,b)

for i in range(N):
    print(answer[i]+1,end=" ")
