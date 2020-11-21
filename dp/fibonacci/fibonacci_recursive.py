'''Use Dynamic Programming approach with recursion to find Nth number in
the fibonacci series.'''

import sys

LIMIT = 900


def f(n):
    if n <= 1:
        return n

    if F[n] is not None:
        return F[n]

    F[n] = f(n - 1) + f(n - 2)
    return F[n]


n = int(input())
if n > LIMIT:
    print('Please enter a number smaller than {LIMIT}')
    sys.exit(1)
elif n < 0:
    print('Please enter a number greater than 0')
    sys.exit(2)

F = [None for i in range(LIMIT)]

F[0] = 0
F[1] = 1

# Nth term is at the index N-1.
fibo = f(n - 1)

print(F[:n])
print(f'fibonacci({n}) = {fibo}')
