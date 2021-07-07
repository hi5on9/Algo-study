def solution(brown, yellow):
    tiles = brown + yellow
    y = 3
    x = 3
    case = []
    answer = [0,0]
    for i in range(y,tiles//2):
        for j in range(x,tiles//2):
            # print(i,j)
            if i<j:break
            if i*j == tiles:
                sero = (brown - j * 2) // 2
                garo = (brown - i * 2) // 2
                if sero * garo == yellow:
                    print(i,j)
                    return [max(i,j),min(i,j)]


    return answer
