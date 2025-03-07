def solution(nums):
    unique_pokemon = len(set(nums))
    max_select = len(nums) // 2
    
    return min(unique_pokemon, max_select)