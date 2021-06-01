def solution(board, moves):
    answer = 0
    stack = []
    
    #for moves
    #   변수 = 해당의 가장 위의것(없을 때 예외처리)
    #   if 이전 요소가 있고, 현재요소와 같으면
    #       answer++, 제거처리
    #   else
    #       스택에 넣기
    for move in moves:
        pick = 0
        for row in board:
            if row[(move-1)] != 0:
                pick = row[(move-1)]
                row[(move-1)] = 0
                break
        if pick == 0:
            continue
        else:
            if len(stack) != 0 and stack[-1] == pick:
                answer += 2
                stack.pop()
            else:
                stack.append(pick)

    return answer