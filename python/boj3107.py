import sys
input = sys.stdin.readline
MAX_NUM = 10000001


a = input().rstrip()
ip = list(a.split(':'))


flag = False
start,end = 0,0
ans = [''] * 8
idx = 0
for i in range(len(ip)):
    if len(ip[i]) != 4 and ip[i]:
        while len(ip[i]) < 4:
            ip[i] = '0' +ip[i]
        ans[idx] = ip[i]
        idx +=1

    elif len(ip[i]) == 4:
        ans[idx] = ip[i]
        idx +=1

    else :
        if not ip[i] and not flag:
            flag = True
            for j in range(8 - len(ip) + 1):
                ans[idx] = '0000'
                idx += 1
        elif not ip[i] and flag:
            ans[idx] = '0000'
            idx += 1


rst = ':'.join(ans)
print(rst)
