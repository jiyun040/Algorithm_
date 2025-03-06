def prime_number():
    M, N = map(int, input().split())
    answer = []
    for i in range(M, N + 1):
        if i < 2:
            continue
        if i == 2:
            answer.append(i)
            continue
        if i % 2 == 0:
           continue
           
        is_prime = True
        for j in range(3, int(i ** 0.5) + 1, 2):
            if i % j == 0:
                is_prime = False
                break
                
        if is_prime:
            answer.append(i)
        
    return answer

for prime in prime_number():
    print(prime)