import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
M = int(input())

cities = [INF] * (N+1)
dist = [[] for _ in range(N+1)]
q = []

def dijkstra(start):
    cities[start] = 0
    heapq.heappush(q,(0,start))

    while q:
        wei, now = heapq.heappop(q)

        if cities[now] < wei:
            continue
        for next_city, w in dist[now]:
            next_wei = wei + w
            if next_wei < cities[next_city]:
                cities[next_city] = next_wei
                heapq.heappush(q,(next_wei,next_city))


for i in range(M):
    u,v,w = map(int,input().split())
    dist[u].append((v,w))

s_city, e_city = map(int,input().split())

dijkstra(s_city)

print(cities[e_city])
