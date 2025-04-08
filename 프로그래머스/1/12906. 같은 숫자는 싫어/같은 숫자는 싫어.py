def solution(arr):
    answer = []
    for i in range(len(arr)):
        if i == 0 or arr[i] != arr[i - 1]: #0 이거나 바로 앞의 숫자와 다르면
            answer.append(arr[i])
            
    return answer