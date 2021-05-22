import sys
import heapq
import math
import re
from collections import deque
from itertools import permutations
input = sys.stdin.readline
MAX_NUM = 10000000

G = int(input())
P = int(input())


def find(g):
    if g == gate[g]:
        return g
    gate[g] = find(gate[g])
    return gate[g]

def union(a,b):
    a = find(a)
    b = find(b)
    gate[a] = b


gate = [i for i in range(G+1)]

rst = 0
for p in range(P):
    g = int(input())
    aaa = find(g)
    # print(aaa)
    if aaa == 0 :
        break
    union(aaa,aaa-1)
    rst+=1

    # print(gate,rst)
    # print(dock)

print(rst)
