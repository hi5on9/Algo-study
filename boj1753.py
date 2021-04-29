import sys
import heapq
input = sys.stdin.readline

INF = sys.maxsize
V, E = map(int,input().split())
K = int(input())
q = []
dist = [INF] * (V+1)
grap = [[] for i in range(V+1)]


def dijkstra(start):
    dist[start] = 0
    heapq.heappush(q,(0,start))


    while q:
        ddd, now = heapq.heappop(q)

        if dist[now] < ddd:
            continue

        for next_node,w in grap[now]:
            temp = ddd + w # 거리 계산한거 ..
            if temp < dist[next_node]:
                dist[next_node] = temp
                heapq.heappush(q,(temp,next_node))



for i in range(E):
    u,v,w = map(int,input().split())
    grap[u].append((v,w))

dijkstra(K)

for i in range(1,V+1):
    if dist[i] == INF:
        print("INF")
    else:
        print(dist[i])
