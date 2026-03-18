import math

def prime(number):
    if number < 1:
        raise ValueError('there is no zeroth prime')
        
    prime_list = []
    candidate = 2

    while len(prime_list) < number:
        is_prime = True

        for j in range(2, int(math.sqrt(candidate)) + 1):
            if candidate % j == 0:
                is_prime = False
                break

        if is_prime:
            prime_list.append(candidate)
            
        candidate += 1

    return prime_list[number - 1]

