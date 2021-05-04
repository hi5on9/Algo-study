import sys
import heapq
from collections import deque
input = sys.stdin.readline
INF = 10000001

N,M = map(int,input().split())
degree = [0] * N
out = [[] for i in range(N)]
for _ in range(M):
    line = list(map(int,input().split()))
    K = line[0]
    pre = line[1] -1
    for i in range(2,K+1):
        cur = line[i] - 1
        out[pre].insert(pre,cur)
        degree[cur] += 1
        pre = cur

# print(out)
q = deque()
ans = []
for i in range(N):
    if degree[i] == 0:
        q.append(i)


# print("--")
while q:
    singer = q.pop()
    ans.append(singer)
    out_line = out[singer]
    # print(out_line)
    # print(degree)
    for i in out_line:
        if degree[i] != 0:
            degree[i] -= 1

        if degree[i] == 0:
            q.append(i)
    # print(degree)

# print("---")
# print(ans)
if sum(degree) != 0:
    print(0)
else:
    for a in ans:
        print(a+1)
