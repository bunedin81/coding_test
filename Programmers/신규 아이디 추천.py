def solution(new_id):
    answer = ''
    
    #Step 1.
    step_one = new_id.lower()
    
    #Step 2.
    temp_len = len(step_one)
    step_two = ""
    for i in range(temp_len):
        if (not step_one[i].isdigit()) and (not step_one[i].isalpha()):
            if step_one[i] in ['.', '-', '_']:
                step_two += (step_one[i])
        else:
            step_two += (step_one[i])
    
    #Step 3.
    while (step_two.find('..') != -1):
        step_two = step_two.replace('..', '.')
    step_three = step_two
    
    #Step 4.
    step_four = step_three
    
    if len(step_three) > 0:
        if step_three[0] == '.':
            step_four = step_three[1:]
    
    if len(step_four) > 0:
        if step_four[-1] == '.':
            step_four = step_four[:-1]
    
    #Step 5.
    step_five = step_four
    if len(step_four) == 0:
        step_five = 'a'
    
    #Step 6.
    step_six = step_five
    if len(step_six) >= 16:
        step_six = step_six[:15]
        
    if len(step_six) > 0:
        if step_six[-1] == '.':
            step_six = step_six[:-1]
    #Step 7.
    step_seven = step_six
    while (len(step_seven) < 3):
        step_seven += (step_seven[-1])
        
    answer = step_seven
        
    return answer
