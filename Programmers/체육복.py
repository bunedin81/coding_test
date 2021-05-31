def solution(n, lost, reserve):
    
    have = 0
    
    #우선적으로 본인의 체육복을 처리
    for i in range(1, n+1):
        if i in lost:
            if i in reserve:
                reserve.remove(i)
                lost.remove(i)
    
    #그 후 타인의 체육복을 처리
    for i in range(1, n+1):
        if i in lost:
            if (i-1) in reserve:
                #해당 학생을 reserve에서 지움
                reserve.remove(i-1)
                #have추가
                have += 1
            elif (i+1) in reserve:
                reserve.remove(i+1)
                have += 1
        else:
            have += 1
    
    return have