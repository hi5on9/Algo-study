import sys
input = sys.stdin.readline
MAX_NUM = 10000000

N, M = map(int,input().split())
nation = [0 for i in range(N+1)]
num = [i for i in range(N+1)]

def union(a,b):
    a = find(a)
    b = find(b)
    if a < b:
        num[b] = a
        nation[a] += nation[b]
    else:
        num[a] = b
        nation[b] += nation[a]

def find(a):
    if a == num[a]:
        return a
    num[a] = find(num[a])
    return num[a]

for n in range(N):
    nation[n+1] = int(input())

for m in range(M):
    O, P, Q = map(int,input().rstrip().split())
    if O == 1 :
        # print("서로 동맹!!")
        union(P,Q)
    elif O == 2:
        # print("전쟁~~~")
        p = find(P)
        q = find(Q)
        if nation[p] < nation[q]:
            nation[q] -= nation[p]
            num[p] = q
        elif nation[p] > nation[q]:
            nation[p] -= nation[q]
            num[q] = p
        elif nation[p] == nation[q]:
            num[p] = 0
            num[q] = 0


    # print(nation)
    # print(num)
    # print("-----")

s = set()
ans = []
for i in range(1,N+1):
    p = find(i)
    if p != 0:
        s.add(find(i))

for i in s:
    ans.append(nation[i])
ans = sorted(ans)
print(len(s))
for i in ans:
    print(i,end=" ")


