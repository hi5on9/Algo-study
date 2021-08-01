import sys
from collections import deque
from itertools import combinations
# input = sys.stdin.readline

def union(a,b):
    aa = find(a)
    bb = find(b)

    if aa != bb:
        num[bb] = aa


def find(a):
    if a == num[a]:
        return a
    num[a] = find(num[a])
    return num[a]


n = int(input())
m = int(input())
num = [i for i in range(n+1)]

for i in range(m):
    a, b = map(int,input().split())
    union(a,b)

# print(num)
cnt = 0

root = find(1)
for i in range(2,n+1):
    if find(num[i]) == root :
        cnt +=1




print(cnt)
