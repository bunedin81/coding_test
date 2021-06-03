def solution(absolutes, signs):
    answer = 0
    answer = sum( [ absolutes[i]*(-1) if signs[i] == False else absolutes[i] for i in range(len(absolutes))] )
    return answer