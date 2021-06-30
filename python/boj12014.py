import sys,copy
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
from collections import deque

T = int(input())

def red(arr):
    stack = [0]
    top = 0
    for a in arr:
        if len(stack)-1 == K:
            return len(stack)-1
        if stack[-1] < a:
            stack.append(a)
            top = a
        else:
            l,h = 0,len(stack)
            while h-l>0:
                m = (l+h) // 2
                if stack[m] < a:
                    l = m+1
                else:
                    h = m
            stack[h] = a

    return len(stack)-1

for t in range(T):
    N,K = map(int,input().split())
    stock = list(map(int,input().split()))

    print("Case #%d"%(t+1))
    length = red(stock)
    if length == K:
        print(1)
    else:
        print(0)
