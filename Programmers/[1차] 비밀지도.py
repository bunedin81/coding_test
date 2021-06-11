def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        val = arr1[i] | arr2[i]
        sq = 1
        bin_val = bin(val)[2:]
        if len(bin_val) != n:
            dif = n - len(bin_val)
            bin_val = "0" * dif + bin_val
            
        row = bin_val.replace("1", "#").replace("0", " ")
        answer.append(row)
    return answer