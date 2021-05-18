import sys
import heapq
import math
import re
from collections import deque
from itertools import permutations
input = sys.stdin.readline


num = [i for i in  range(1004000)]
num[1] = 0

for i in range(2,len(num)):
    if num[i] == 0:
        continue
    else:
        for j in range(i*2,len(num),i):
            num[j] = 0


sosu = []
N = int(input())
i = N 
while True:
    if num[i] != 0:
        word = reversed(str(num[i]))
        pal = int("".join(word))
        if pal == i:
            print(num[i])
            break

    i +=1






