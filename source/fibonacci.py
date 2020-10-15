from functools import reduce
MAX_FIBONACCI_VALUE = 1000


def fibonacci_calc(count):
    posint = int(count)
    assert isinstance(posint, int)
    assert posint >= 0

    sequence = [0, 1]
    if posint > 2:
        for f in range(2, posint):
            parent = sequence[-1]
            grandparent = sequence[-2]
            sequence.append(grandparent + parent)
    return sequence[:posint], posint


def get_summing_subsets(set_arr, target):
    finish = []
    working = [[]]
    while len(working):
        next_work = []
        for i in range(len(working)):
            for j in range(len(set_arr)):
                subset = working[i] + [set_arr[j]]
                sum_val = reduce((lambda x, y: x + y), subset)
                if sum_val <= target:
                    if sum_val == target:
                        finish.append(subset)
                    else:
                        next_work.append(subset)
        working = next_work
    return finish


def fibonacci_combinations(number):
    fibonacci_series, number = fibonacci_calc(number)
    valid_fib_numbers = list(
        filter(lambda x: 1 < x < number, fibonacci_series))
    return get_summing_subsets(valid_fib_numbers, number)



if __name__ == "__main__":
    result = fibonacci_combinations(7)
    print(result)
    # for i in result:
    #    print(i)
