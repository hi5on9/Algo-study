import sys
input = sys.stdin.readline
from bisect import bisect_left
from collections import deque
MAX_NUM = 10000000

N = int(input())
num = list(map(int,input().split()))

q = []


q.append(num[0])
t = []
for i in num:
    if q[-1] < i:
        q.append(i)
        t.append((len(q)-1,i))

    else :
        idx = bisect_left(q,i)
        q[idx] = i
        t.append((idx,i))

last_idx = len(q)-1
# print(t)
# print(q)

ans = []
for i in range(N-1,-1,-1):
    if t[i][0] == last_idx:
        ans.append(t[i][1])
        last_idx -= 1

print(len(q))
print(*reversed(ans))
