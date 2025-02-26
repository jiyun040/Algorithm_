def solution(t, p):
    p_len = len(p)
    p_int = int(p)
    count = 0

    for i in range(len(t) - p_len + 1):
        sub_str = t[i:i + p_len]
        if int(sub_str) <= p_int:
            count += 1
    
    return count