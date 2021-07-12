import sys
input = sys.stdin.readline

l,w,h = map(int,input().split())
n = int(input())

cube = [0] * 21

#box = [[[0 for col in range(l)] for row in range(w)] for depth in range(h)]


for i in range(n):
    a,b = map(int,input().split())
    cube[a] +=b

total = 0
cnt = 0
for i in range(19,-1,-1):
    total <<= 3
    t = min(cube[i],(l>>i)*(w>>i)*(h>>i)- total)
    total += t
    cnt += t

if total == l*w*h:
    print(cnt)
else:
    print(-1)
