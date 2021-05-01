import sys
import heapq
input = sys.stdin.readline
INF = 10000001


N = int(input())
stars = []
stella = [i for i in range(N)]
for _ in range(N):
    a, b = map(float,input().split())
    stars.append([a,b])

lll = []
for i in range(N):
    for j in range(i+1,N):
        if i == j : continue
        dis = ((stars[i][0] - stars[j][0])**2 + (stars[i][1]-stars[j][1])**2) ** 0.5
        lll.append([i,j,dis])

lll = sorted(lll,key=lambda x:x[2])
# print(lll)

def find(a):
    if stella[a] == a:
        return a
    stella[a] = find(stella[a])
    return stella[a]

def union(a,b):
    aa = find(a)
    bb = find(b)
    if aa == bb: return False
    stella[b] = a
    return True

rst = 0
for a,b,c in lll:
    aa = find(a)
    bb = find(b)

    if union(aa,bb):
        rst += c
print(round(rst,2))
