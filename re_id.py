'''
Name: Kevin Douglass
School: CSU, Chico
Major: Computer Science,
Minor: Mathematics
Date: 12/1/20
'''
##########################


def is_prime(num):
    """Returns True if the number is prime
    else False."""
    if num == 0 or num == 1:
        return False
    for x in range(2, num):
        if num % x == 0:
            return False
    else:
        return True
    
def gen_p():
    primes = [str(x) for x in range(1000) if is_prime(x)]
    return primes

def sol(i):
    pri = gen_p()
    sol = ''.join(pri)
    # pri = ''.join([str(x) for x in range(100) if is_prime(x)])[:5]
    return sol[i:i+5]


############################
# This main method was only used to test my code. Only content above 'main' was used.
if __name__ == "__main__":
    #pass
    idx:int = 0
    print('Printing solution to prime_ids-index {}'.format(idx))
    print(sol(idx))


