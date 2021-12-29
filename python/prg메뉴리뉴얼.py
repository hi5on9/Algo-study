def solution(orders, course):
    answer = set()
    for c in course:
        comb_alpha = []
        for o in orders:
            temp = list(o)
            temp.sort()
            comb_alpha += list(combinations(temp, c))
        for i in range(len(comb_alpha)):
            comb_alpha[i] = ''.join(comb_alpha[i])
        if len(comb_alpha) <1 :
            continue
        comb_alpha.sort()
        cnt = [0] * len(comb_alpha)
        for i in range(len(comb_alpha)):
             for o in orders:
                 flag = True
                 for j in list(comb_alpha[i]):
                    if j not in o:
                        flag = False
                 if flag:
                    cnt[i] += 1
        max_value = max(cnt)
        max_index = list(filter(lambda x:cnt[x] == max_value, range(len(cnt))))
        if max_value > 1:
            for i in max_index:
                answer.add(''.join(comb_alpha[i]))
        # print("answer:: ",answer)
    answer = list(answer)
    answer.sort()
    print(answer)
    return answer
