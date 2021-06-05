from collections import deque

def solution(numbers, hand):
    answer = ''
    l_pos = '*'
    r_pos = '#'
    num_dict = {
        1:[2, 4],
        2:[1, 3, 5],
        3:[2, 6],
        4:[1, 5, 7],
        5:[2, 4, 6, 8],
        6:[3, 5, 9],
        7:[4, 8, '*'],
        8:[5, 7, 9, 0],
        9:[6, 8, '#'],
        '*':[7, 0],
        0:[8, '*', '#'],
        '#':[9, 0]
    }
    
    for number in numbers:
        if number in [1, 4, 7, '*']:
            l_pos = number
            answer += 'L'
        elif number in [3, 6, 9, '#']:
            r_pos = number
            answer += 'R'
        else:
            l_dist = get_distance_bfs(num_dict, l_pos, number)
            r_dist = get_distance_bfs(num_dict, r_pos, number)
            if l_dist == r_dist:
                if hand == "right":
                    r_pos = number
                    answer += 'R'
                elif hand == "left":
                    l_pos = number
                    answer += 'L'
            elif l_dist > r_dist:
                r_pos = number
                answer += 'R'
            else:
                l_pos = number
                answer += 'L'

    return answer

def get_distance_bfs(num_dict, now, obj):
    visited = []
    queue = deque([now])
    distance = deque([0])
    
    while queue:
        n = queue.popleft()
        now_distance = distance.popleft()
        if n == obj:
            return now_distance
        if n not in visited:
            visited.append(n)
            for ele in num_dict[n]:
                if ele not in visited:
                    queue.append(ele)
                    distance.append(now_distance+1)