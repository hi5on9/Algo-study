import sys
import heapq
from collections import deque
input = sys.stdin.readline

T = int(input())

for t in range(T):
    clothes = {}
    N = int(input())
    for n in range(N):
        a,b = input().split()
        temp = set()
        if clothes.get(b) :
            Z = clothes.get(b)
            for z in Z:
                temp.add(z)
        temp.add(a)
        clothes[b] = temp

    # print(clothes)

    ans = 1
    for c in clothes:
        ans *= (len(clothes[c]) +1)
        # print(len(clothes[c]))
    # if len(clothes) <= 1: ans = 0
    print(ans-1)

