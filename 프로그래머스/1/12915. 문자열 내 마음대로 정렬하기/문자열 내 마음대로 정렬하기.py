def solution(strings, n):
    # 반복문을 돌면서 strings의 n번째의 알파벳들을 비교
    index_chars = []
    for s in strings:
        index_chars.append((s[n], s))
    index_chars.sort()
    
    # 알파벳들 중에 제일 빠른 알파벳의 총 단어를 순서대로 출력
    sorted_strings = []
    for s in index_chars:
        sorted_strings.append(s[1])
        
    return sorted_strings