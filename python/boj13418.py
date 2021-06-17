import sys
import heapq
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())
graph = []
road = [i for i in range(N+1)]
start = 0
for m in range(M+1):
    a,b,c = map(int,input().split())
    if a == 0:
        if c == 0: start = 1
        continue
    graph.append([a,b,c])



def find(a):
    if road[a] == a:
        return a
    road[a] = find(road[a])
    return road[a]

def union(a,b):
    a = find(a)
    b = find(b)
    if a!= b:
        road[b] = a
        return True
    return False

graph = sorted(graph,key=lambda x:(x[2]))

# print("--MAX TIRED--")
# for i in graph:
#     print(i)
max_tired = start
for a,b,c in graph:
    a = find(a)
    b = find(b)
    if union(a,b):
        if c ==0: max_tired +=1

graph = sorted(graph,key=lambda x:(x[2]),reverse=True)
# print("--MIN TIRED--")
# for i in graph:
#     print(i)
min_tired = start
road = [i for i in range(N+1)]
for a,b,c in graph:
    a = find(a)
    b = find(b)
    if union(a,b):
        if c ==0: min_tired +=1

print(max_tired**2-min_tired**2)
