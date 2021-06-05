import sys
input = sys.stdin.readline
MAX_NUM = 10000001


num = input().rstrip()
a = num.split("-")
ans = []
for i in range(len(a)):
    cnt = 0
    s = a[i].split("+")
    for j in s:
        cnt += int(j)
    ans.append(cnt)

rst = ans[0]

for i in range(1,len(ans)):
    rst -= ans[i]

print(rst)
