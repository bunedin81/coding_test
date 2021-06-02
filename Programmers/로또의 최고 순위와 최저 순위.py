def solution(lottos, win_nums):
    #우선, lottos와 win_nums중 맞는 것을 count
    #최고 당첨등급은 0이 맞았을 때
    #최저 당첨등급은 0이 틀렸을 때
    answer = []
    count_0 = 0
    count_match = 0
    
    #보이지 않는 숫자의 개수
    for i in lottos:
        if i == 0:
            count_0 += 1
    
    #일치하는 수의 개수
    for i in win_nums:
        if i in lottos:
            count_match += 1
    
    #최고 당첨등급
    max_rank = 7 - (count_0 + count_match)
    if max_rank == 7:
        max_rank = 6
    
    #최저 당첨등급
    min_rank = 7 - count_match
    if min_rank == 7:
        min_rank = 6
    
    answer.append(max_rank)
    answer.append(min_rank)
    
    return answer