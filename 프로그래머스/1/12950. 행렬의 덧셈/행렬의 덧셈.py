def solution(arr1, arr2):
    answer =[]
    
    for i in range(len(arr1)):
        row = []
        for j in range(len(arr1[i])): # 각 행의 열을 반복, arr2로 하게 된다면 arr2[i]의 크기를 넘는 것을 찾게 됨
            row.append(arr1[i][j] + arr2[i][j])
        answer.append(row)
    
    return answer