def solution(s):
    answer = []
    last_seen = {}  # 각 문자의 최근 등장 인덱스 저장

    for i, char in enumerate(s):
        if char in last_seen:  # 이전에 등장한 적 있는 경우
            answer.append(i - last_seen[char])
        else:  # 처음 등장한 경우
            answer.append(-1)
        
        last_seen[char] = i  # 현재 인덱스를 저장

    return answer