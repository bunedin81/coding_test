def solution(N, stages):
    answer = []
    triers = [0 for i in range(N)]
    clearer = [0 for i in range(N)]
    rank = []
    
    #우회하면서 도전자, 성공자 찾기
    for i in stages:
        if i <= N:
            triers[i-1] += 1
        if i > N:
            for j in range(len(clearer)):
                clearer[j] += 1
        else:
            for j in range(i):
                clearer[j] += 1
                
    for i in range(len(triers)):
        if clearer[i] == 0:
            rank.append([i+1, 0])
        else:
            rank.append([i+1, triers[i]/clearer[i]])
    
    temp = sorted(rank, key=lambda x:-x[1])
    for t in temp:
        answer.append(t[0])
    
    
    return answer