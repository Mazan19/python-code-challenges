import math
import sys

### get_prime_factor() func for Finding prime factors for number N
### Prime factors for number N is a list of numbers which multiplying got N 
### Expexted results: 13 - [13];  10 - [2,5]; 152 - [2,2,2,19] 
### ToDo: calculation for negative numbers, fool test

def get_prime_factor(n):
    
    def get_nd(x):
        for i in range(2,round(math.sqrt(x))):
            if x % i == 0:
                return i
        return int(x)

    tmp_n = n
    numbers = []
    while (tmp_n>1):
        a = get_nd(tmp_n)
        tmp_n /= a
        numbers.append(a)
    return numbers


if __name__ == "__main__":
    result = get_prime_factor(10)
    print(result)
