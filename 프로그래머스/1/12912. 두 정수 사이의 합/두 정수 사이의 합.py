def solution(a, b):
    if a == b:
        return a
    else:
        return sum(range(min(a, b), max(a, b) + 1))