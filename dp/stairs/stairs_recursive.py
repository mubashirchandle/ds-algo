'''Find the number of possible combination that can be used to go up `n` steps
where every move is either `1` or `2` step.'''

previous_results = None  # Memoised results


def find_num_of_combinations(n):
    global previous_results

    if previous_results is None:
        previous_results = [None for _ in range(n + 1)]

    if n == 1 or n == 2:
        previous_results[n] = n
        return n
    elif previous_results[n]:
        return previous_results[n]

    n_1 = find_num_of_combinations(n - 1)
    n_2 = find_num_of_combinations(n - 2)

    previous_results[n - 1] = n_1
    previous_results[n - 2] = n_2
    previous_results[n] = n_1 + n_2

    return n_1 + n_2


n = int(input('Enter the number of steps: '))

n_combinations = find_num_of_combinations(n)
print(f'Number of combinations: {n_combinations}')
