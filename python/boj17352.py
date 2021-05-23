import sys
input = sys.stdin.readline
MAX_NUM = 10000000

N = int(input())
bridge = [i for i in range(N)]

def find(a):
    if a == bridge[a]:
        return a
    bridge[a] = find(bridge[a])
    return bridge[a]

def union(a,b):
    a = find(a)
    b = find(b)

    if a != b:
        bridge[b] = a

for n in range(N-2):
    a, b = map(int,input().split())
    aa = find(a-1)
    bb = find(b-1)
    # print(aa,bb)
    if aa != bb:
        union(aa,bb)
    # print(bridge)

for b in range(len(bridge)):
    if b == bridge[b]:
        print(b+1,end=" ")
