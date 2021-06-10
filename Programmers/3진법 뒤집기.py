def solution(n):
    answer = 0
    
    pos_val = []
    
    if n < 3:
        return n
    
    while n >= 3:
        na = n%3
        n = n//3

        pos_val.insert(0, na)
    if n != 0:
        pos_val.insert(0, n)
    
    three_sq = 1
    for i in pos_val:
        answer += i * three_sq
        three_sq *= 3
    
    return answer