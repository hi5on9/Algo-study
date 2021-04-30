import sys
import heapq
input = sys.stdin.readline
INF = 10000001

N = int(input())
M = int(input())

graph = [[INF for _ in range(N+1)] for _ in range(N+1)]

for i in range(N):
    graph[i][i] = 0

for i in range(M):
    u,v,w = map(int,input().split())
    graph[u-1][v-1] = min(graph[u-1][v-1],w)

for k in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])


for i in range(N):
    for j in range(N):
        if graph[i][j] == INF:
            print(0,end=" ")
        else : print(graph[i][j],end=" ")
    print()






