def solution(nums):
    answer = 0

    for first in range(len(nums)-2):
        for second in range(first+1, len(nums)-1):
            for third in range(second+1, len(nums)):
                answer += is_prime(nums[first] + nums[second] + nums[third])
                
    return answer

#소수를 구하는 함수
def is_prime(num):
    for i in range(2, num):
        if num%i == 0:
            return False
    return True