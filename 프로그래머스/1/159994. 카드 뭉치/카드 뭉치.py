def solution(cards1, cards2, goal):
    index1, index2 = 0, 0 # 각각의 인덱스
    len1, len2 = len(cards1), len(cards2) # 각각의 길이
    
    # goal를 돌면서
    for word in goal:
        # 만약 cards1의 index가 word와 같다면 index 1 증가
        if index1 < len1 and cards1[index1] == word:
            index1 += 1
        # 만약 cards2의 index가 word와 같다면 index 1 증가
        elif index2 < len2 and cards2[index2] == word:
            index2 += 1
        # 같은게 하나도 없다면 No 출력
        else:
            return "No"
    
    # 위의 조건을 만족한다면 Yes 출력
    return "Yes"
    
    