'''Find the number of possible combination that can be used to go up `n` steps
where every move is either `1` or `2` step.'''

LIMIT = 100_000


def find_num_of_combinations(n):
    results = [None] * (n + 1)

    results[1], results[2] = 1, 2

    for i in range(3, n + 1):
        results[i] = results[i - 1] + results[i - 2]

    return results[-1]


n = int(input('Enter the number of steps: '))

if n > LIMIT:
    print(f'Please enter a number smaller than {LIMIT:,}')
else:
    n_combinations = find_num_of_combinations(n)
    print(f'Number of combinations: {n_combinations}')
