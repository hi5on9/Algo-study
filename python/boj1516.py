import sys
import heapq
from collections import deque
input = sys.stdin.readline
INF = 10000001

N = int(input())
time = [0] * N
indegree = [0] * N
building = [[] for _ in range(N)]

for i in range(N):
    l = list(map(int,input().split()))
    time[i] = l[0]

    # print(len(l))
    if len(l) < 2:
        continue
    else:
        prev = l[1] -1
        for j in range(1,len(l)-1):
            cur = l[j] -1
            indegree[i] += 1
            building[cur].insert(cur,i)




q = deque()

for i in range(N):
    if indegree[i] == 0 :
        q.append(i)

ans = []
rst = [time[i] for i in range(N)]
# print(rst)
while q:
    num = q.pop()
    ans.append(num)
    order = building[num]

    for o in order:
        if indegree[o] != 0 :
            indegree[o] -= 1
        if indegree[o] == 0:
            q.append(o)

# print(ans)

for a in ans:
    # print(a,building[a])
    for b in building[a]:
        # print(rst[a],rst[b],time[b])
        rst[b] = max(rst[b],rst[a]+time[b])
        # print(rst[b])
for a in rst: print(a)



