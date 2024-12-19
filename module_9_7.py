
def is_prime(f):
    def prime(*args):
        rf = f(*args)
        is_primes = True
        for j in range(2, rf):
            if rf % j == 0:
                is_primes = False
                break
        if is_primes:
            print('Простое')
        else:
            print('Составное')
        return rf
    return prime

@is_prime
def sum_three(a, b, c):
    r = a + b + c
    return r

result = sum_three(2, 3, 6)

print(result)