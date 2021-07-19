import sys,copy
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
from collections import deque
from itertools import permutations

N = int(input())
num = [i for i in range(1,N+1)]
ans = list(map(int,input().split()))

def pre_per(arr):
    l = len(arr) - 1
    i,j,k = [l for _ in range(3)]

    while i > 0 and arr[i-1] <= arr[i]:
        i -=1

    if not i:
        return 0;

    while arr[i-1] <= arr[j]:
        j -= 1

    arr[i-1],arr[j] = arr[j], arr[i-1]

    while i < k:
        arr[i],arr[k] = arr[k],arr[i]
        i+=1
        k-=1

    return arr


ans = pre_per(ans)
print(-1) if not ans else print(*ans)
