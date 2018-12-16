import math
def is_prime(n):
    if n == 2:
        return 'Prime'
    if n % 2 == 0 or n < 2:
        return 'Not prime'
    for j in range(3, int(math.sqrt(n)) + 1):
        if n % j == 0:
            return 'Not prime'
    return 'Prime'


n = int(input())
for i in range(n):
    number = int(input())
    print(is_prime(number))
    

