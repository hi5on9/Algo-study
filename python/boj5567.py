import sys
input = sys.stdin.readline
from collections import deque
from itertools import combinations

N = int(input())
M = int(input())
relationship = [[] for _ in range(N)]
invited = [0] * N
for i in range(M):
    a,b = map(int,input().split())
    relationship[a-1].append(b-1)
    relationship[b-1].append(a-1)



q = deque()
invited[0] = 1
q.append(0)

while q:
    a = q.popleft()
    for i in relationship[a]:
        if invited[i] == 0:
            invited[i] = invited[a] + 1
            q.append(i)

# print(invited)


# print(invited)
ans = 0
for r in invited:
    if 1 < r <= 3:
        ans +=1

print(ans)
