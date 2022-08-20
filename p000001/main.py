from euler.Number import Number


def search_numbers_sum(range_limit: int, factors: list[int]):
    searched_sum: int = 0
    for n in range(1, range_limit):
        multiplications: list[int] = Number.is_multiplication_of_any_factor(factors, n)
        if len(multiplications) > 0:
            searched_sum += n

    return searched_sum


print(f'searched_numbers sum : {search_numbers_sum(10, [3, 5])}')

print(f'searched_numbers sum : {search_numbers_sum(1000, [3, 5])}')
