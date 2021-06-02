import sys
input = sys.stdin.readline
MAX_NUM = 10000001

N = int(input())
graph = []
planet = [i for i in range(N)]
for n in range(N):
    x,y,z = map(int,input().split())
    graph.append([x,y,z,n])

dis = []
for i in range(3):
    graph = sorted(graph,key = lambda x:x[i])
    for j in range(1,N):
        x = graph[j][i]
        _from = graph[j][3]
        xx = graph[j-1][i]
        _to = graph[j-1][3]
        d = abs(xx-x)
        dis.append([_from,_to,d])

def find(a):
    if a == planet[a]:
        return a
    planet[a] = find(planet[a])
    return planet[a]

def union(a,b):
    a = find(a)
    b = find(b)
    if a == b:
        return False
    planet[b] = a
    return True


dis = sorted(dis,key=lambda x:x[2])
# print(dis)
ans = 0
for x,y,dis in dis:
    x = find(x)
    y = find(y)
    if union(x,y):
        ans += dis



print(ans)



