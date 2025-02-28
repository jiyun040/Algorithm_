def solution(name, yearning, photo):
    score_map = {}
    for i in range(len(name)): # name 리스트의 길이만큼 반복
        key = name[i] # name의 i번째 요소
        value = yearning[i] # yearing의 i번째 요소
        score_map[key] = value # 딕셔너리에 추가
    
    result = []
    
    for p in photo: # 사진을 하나씩 처리, p는 사진에 나온 사람의 이름
        total_score = 0
        for person in p: # 각 사진에서 나온 사람들을 한명씩 처리
            if person in score_map:
                total_score += score_map[person]
            else:
                total_score += 0
        result.append(total_score)
        
    return result