def solution(numLog):
    answer = ""
    for i in range(len(numLog)-1):
        if numLog[i+1] - numLog[i] == 1:
            res = "w"
        elif numLog[i+1] - numLog[i] == -1:
            res = "s"
        elif numLog[i+1] - numLog[i] == 10:
            res = "d"
        else:
            res = "a"
        answer += res
    return answer