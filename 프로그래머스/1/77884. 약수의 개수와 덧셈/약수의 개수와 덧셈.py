import math

def solution(left, right):
    answer = 0
    for num in range(left, right + 1):
        if math.sqrt(num) % 1 == 0: # 제곱수 여부 확인
            answer -= num
        else:
            answer += num
    return answer