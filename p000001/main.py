def is_multiplication_of_any_factor(factors: list[int], checked_number: int):
    multiplications: list[int] = []
    for current_factor in factors:
        is_multiplication: bool = checked_number % current_factor == 0
        if is_multiplication:
            multiplications.append(current_factor)
    return multiplications


def search_numbers_sum(range_limit: int, factors: list[int]):
    searched_numbers: list[int] = []
    searched_sum: int = 0
    for n in range(1, range_limit):
        multiplications: list[int] = is_multiplication_of_any_factor(factors, n)
        if len(multiplications) > 0:
            searched_numbers.append(n)
            searched_sum += n

    return searched_sum


print(f'searched_numbers sum : {search_numbers_sum(10, [3, 5])}')

print(f'searched_numbers sum : {search_numbers_sum(1000, [3, 5])}')
