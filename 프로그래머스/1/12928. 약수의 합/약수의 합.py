def solution(n):
    if n == 0:
        return 0
    answer = 0
    
    for i in range (1, int(n ** 0.5) + 1): # 1부너 루트2 + 1까지 검사
        if n % i == 0: # i가 약수라면
            answer += i
            if i != n // i: # 중복으로 더해지는 것 방지, 16일경우 4*4이기에 한 번만 더해야 함
                answer += n // i
    return answer