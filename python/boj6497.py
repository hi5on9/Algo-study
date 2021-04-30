import sys
import heapq
input = sys.stdin.readline
INF = 10000001

def find(a):
    if house[a] == a:
        return a
    house[a] = find(house[a])
    return house[a]

def union(a,b):
    aa = find(a)
    bb = find(b)
    if aa == bb : return False
    house[b] = a
    return True

while(True):
    N, M = map(int, input().split())
    if (N ==0 and M ==0) : break
    light = []
    house = [i for i in range(N)]
    total = 0

    for _ in range(M):
        x,y,z = map(int,input().split())
        light.append([x,y,z])
        total += z

    light = sorted(light,key=lambda x:x[2])

    rst = 0

    for a,b,c in light:
        aa = find(a)
        bb = find(b)
        if union(aa,bb):
            rst +=c

    print(total-rst)


