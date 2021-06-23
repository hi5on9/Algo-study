import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

from collections import deque

N,M = map(int,input().split())
indegree = [[i,0] for i in range(N+1)]
degree = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    indegree[b][1] += 1
    degree[a].append(b)

q = deque()
v = [0] * (N+1)
for i in range(1,N+1):
    if indegree[i][1] == 0:
        q.append(indegree[i])
        v[i] = 1

while q:
    idx,d = q.popleft()
    print(idx,end=" ")

    for i in degree[idx]:
        if indegree[i][1] !=0:
            indegree[i][1] -= 1
        if indegree[i][1] == 0 and v[i] == 0:
            q.append(indegree[i])

