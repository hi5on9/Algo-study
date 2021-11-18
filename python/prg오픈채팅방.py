def solution(record):
    sentence = []
    users = {}
    for r in record:
        msg = r.split()
        if msg[0] == "Enter":
            users[msg[1]] = msg[2]
            kor = "님이 들어왔습니다."
            sentence.append([msg[1],kor])
        elif msg[0] == "Change":
            users[msg[1]] = msg[2]
        elif msg[0] == "Leave":
            kor = "님이 나갔습니다."
            sentence.append([msg[1],kor])


    answer = []
    for s in sentence:
        msg = users[s[0]] + s[1]
        answer.append(msg)

    return answer
