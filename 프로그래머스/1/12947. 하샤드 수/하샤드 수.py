def solution(x):
    plus = sum(map(int, str(x)))
    
    if x % plus == 0:
        return True
    else:
        return False