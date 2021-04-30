import sys
import heapq
input = sys.stdin.readline
INF = 10000001

N = int(input())


graph = [[INF] for _ in range(N)]

for i in range(N):
    graph[i] = list(map(int,input().split()))

for i in range(N):
    for j in range(N):
        if graph[i][j] == 0 : graph[i][j] = INF

# print(graph)

for k in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])


for i in range(N):
    for j in range(N):
        if graph[i][j] == INF:
            print(0,end=" ")
        else : print(1,end=" ")
    print()






