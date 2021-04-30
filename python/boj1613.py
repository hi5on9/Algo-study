import sys
import heapq
input = sys.stdin.readline
INF = 10000001

N,M = map(int,input().split())
graph = [[INF for _ in range(N)]for _ in range(N)]
graph2 = [[INF for _ in range(N)]for _ in range(N)]

for i in range(N):
    graph[i][i] = 0
    graph2[i][i] = 0  # 뒤 사건 먼저

for _ in range(M):
    a,b = map(int,input().split())
    graph[a-1][b-1] = 1
    graph2[b-1][a-1] = 1



for k in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])
            graph2[i][j] = min(graph2[i][j], graph2[i][k] + graph2[k][j])


# for i in range(N):
#     print(*graph[i])
#
# print("===")
#
# for i in range(N):
#     print(*graph2[i])



S = int(input())
for _ in range(S):
    a,b = map(int,input().split())
    first = graph[a-1][b-1]
    second = graph2[a-1][b-1]

    if first == second == INF:
        print(0)
    elif first == INF and second!=INF:
        print(1)
    elif second==INF and first != INF:
        print(-1)
