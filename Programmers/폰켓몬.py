def solution(nums):
    #pick = 절반
    #nums를 unique하게 바꾼다.
    #nums.length가 pick보다 작으면
    #   답은 nums.length가 됨
    #nums.length가 pcik보다 크거나 같으면
    #   답은 pick이 됨    
    answer = 0    
    pick = len(nums)/2
    uniq_nums = []
    
    for i in range(len(nums)):
        if nums[i] not in uniq_nums:
            uniq_nums.append(nums[i])
    if len(uniq_nums) < pick:
        answer = len(uniq_nums)
    else:
        answer = pick
    
    return answer