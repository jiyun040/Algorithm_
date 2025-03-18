def solution(phone_number):
    
    stars = '*' * (len(phone_number) - 4) # 뒤 4자리 제외하고 *로 결정

    last_four_numbers = phone_number[-4:] # 폰번호의 뒷자리 4번호 슬라이싱 해 저장
    
    return stars + last_four_numbers # 앞자리의 *과 뒷 4자리를 붙여서 출력