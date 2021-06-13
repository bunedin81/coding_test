import re

def solution(dartResult):
    answer = 0
    p = re.compile('[0-9]+[A-Z]+\W*')
    m = p.findall(dartResult)
    
    each = []
    for i in range(len(m)):
        bonus = 1
        p = re.compile('[0-9]')
        temp = p.findall(m[i])
        if len(temp) > 1:
            num = 10
        else:
            num = int(temp[0])
        
        p = re.compile('[A-Z]')
        power = p.findall(m[i])[0]
        
        p = re.compile('\W+')
        
        temp = p.findall(m[i])
        if len(temp) > 0:
            bonus_ = temp[0]
        else:
            bonus_ = ''
        #print(bonus_)
        
        if power == 'S':
            power = 1
        elif power == 'D':
            power = 2
        elif power == 'T':
            power = 3
        
        if bonus_ == '#':
            bonus = -1
        elif bonus_ == '*':
            bonus = 2
            if i >0:
                each[i-1] *= 2
        else:
            bonus = 1
        each.append(bonus*(num**power))
        
    print(each)
    answer = sum(each)
    return answer