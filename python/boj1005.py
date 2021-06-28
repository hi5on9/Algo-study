import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
from collections import deque

T = int(input())
for t in range(T):
    N,K = map(int,input().split())
    graph = [[] for _ in range(N + 1)]
    indegree = [0] * (N+1)
    times = [0] + list(map(int,input().split()))
    for k in range(K):
        a,b = map(int,input().split())
        indegree[b] += 1
        graph[a].append(b)
    D = int(input())

    cnt = 0
    sum_time = [0] * (N+1)
    q = deque()
    for idx, i in enumerate(indegree):
        if i == 0 and idx >0:
            q.append(idx)
            sum_time[idx] = times[idx]
    ans = []

    # print(indegree)
    # print(graph)
    while q:
        idx = q.popleft()
        ans.append(idx)
        max_time = 0
        for i in graph[idx]:
            sum_time[i] = max(times[i] + sum_time[idx],sum_time[i])
            if indegree[i] != 0:
                indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
        cnt += 1

    # print(ans)
    # print(sum_time)
    print(sum_time[D])
    # print("=======")
