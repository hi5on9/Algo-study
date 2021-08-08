def solution(answers):
    answer = []
    score = [0, 0, 0]
    o_ans = [1, 2, 3, 4, 5]
    s_ans = [2, 1, 2, 3, 2, 4, 2, 5]
    t_ans = [3, 3, 1, 1, 2, 2, 4, 4, 5,5]
    for idx,a in enumerate(answers):
        one = idx % 5
        two = idx % 8
        three = idx % 10
        if o_ans[one] == a:
            score[0] += 1
        if s_ans[two] == a:
            score[1] += 1
        if t_ans[three] ==a:
            score[2] += 1

    max_score = max(score)
    # print(score)
    if max_score!=0:
        for idx,s in enumerate(score):
            if max_score==s:
                answer.append(idx+1)
    print(answer)
    return answer
