def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def turing_machine(unary_input):
    return is_prime(len(unary_input))
