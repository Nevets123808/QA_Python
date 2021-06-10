def is_prime(x):
    breakpoint()
    if x < 2:
        return False
    else:
        for n in range(2, x-1):
            if x % n == 0:
                return False
        return True

print(is_prime(7))