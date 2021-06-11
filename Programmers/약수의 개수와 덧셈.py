def solution(left, right):
    answer = 0
    
    for i in range(left, right+1):
        answer += get_ali_result(i) * i
    return answer

def get_ali_result(value):
    temp = 0
    for i in range(1, value+1):
        if value%i == 0:
            temp += 1
    return 1 if temp%2 == 0 else -1 