def solution(price, money, count):
    # 1부터 count까지 price와 곱한 값들을 모두 더함
    total = 0
    for i in range(1, count + 1):
        total += price * i
    return max(0, total - money)