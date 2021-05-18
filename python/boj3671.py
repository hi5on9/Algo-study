import sys
import heapq
import math
import re
from collections import deque
from itertools import permutations
input = sys.stdin.readline
MAX_NUM = 10000000
num = [i for i in range(MAX_NUM)]
flag = [0] * MAX_NUM
num[1] = 0
for i in range(2,len(num)):
    if num[i] == 0 :continue
    else:
        for j in range(2*i,len(num),i):
            num[j] = 0

T = int(input())
for t in range(T):
    C = list(map(str,input().strip()))
    ans = 0
    for j in range(1,len(C)+1):
        numbers = list(map(''.join,permutations(C,j)))
        for n in numbers:
            n = int(n)
            if flag[n] == t+1: continue
            else:
                flag[n] =t+1
                if num[n] !=0 : ans +=1

    print(ans)



