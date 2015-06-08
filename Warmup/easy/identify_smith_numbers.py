def get_prime_factors(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac


def is_smith(n):
    total = sum(map(int, str(n)))

    prime_factors = get_prime_factors(n)
    summ_primes = 0
    for pf in prime_factors:
        summ_primes += sum(map(int, str(pf)))

    if total == summ_primes:
        return 1
    return 0


n = int(raw_input())
print is_smith(n)
