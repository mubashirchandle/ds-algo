'''Use Dynamic Programming approach with iteration to find Nth number in
the fibonacci series.'''

import sys

LIMIT = 900

n = int(input())
if n > LIMIT:
    print('Please enter a number smaller than {LIMIT}')
    sys.exit(1)
elif n < 0:
    print('Please enter a number greater than 0')
    sys.exit(2)

F = [0, 1]

for i in range(2, LIMIT):
    F.append(F[i - 1] + F[i - 2])

# Nth term is at the index N-1.
fibo = F[n - 1]

print(F[:n])
print(f'fibonacci({n}) = {fibo}')
