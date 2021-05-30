import sys
input = sys.stdin.readline
from bisect import bisect_left
from collections import deque
MAX_NUM = 10000000

N,K = map(int,input().split())
if N == K :
    print(0)
    exit(0)
q = deque()

q.append([N,0])

ans = []
loc = set()
while q:
    where , t = q.popleft()
    arr = [where*2,where-1,where+1]
    for a in arr:
        if a == K:
            print(t+1)
            q.clear()
            break
        if a not in loc and 0<= a <=100000:
            q.append([a,t+1])
            loc.add(a)


