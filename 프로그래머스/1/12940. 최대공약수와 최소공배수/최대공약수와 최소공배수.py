import math

def solution(n, m):
    # 최대공약수
    gcd = math.gcd(n, m)
    # 최소공배수
    lcm = (n * m) // gcd
    return [gcd, lcm]