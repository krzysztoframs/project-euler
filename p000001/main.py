def search_numbers_sum(range_limit: int):
    searched_numbers: list[int] = []
    searched_sum: int = 0
    for n in range(1, range_limit):
        multiply_of_three: bool = n % 3 == 0
        multiply_of_five: bool = n % 5 == 0
        if multiply_of_five or multiply_of_three:
            searched_numbers.append(n)
            searched_sum += n

    return searched_sum


print(f'searched_numbers sum : {search_numbers_sum(10)}')

print(f'searched_numbers sum : {search_numbers_sum(1000)}')
