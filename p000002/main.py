from euler.Fibonacci import Fibonacci

from euler.Number import Number


def fibonacci(limit: int) -> int:
    fib: Fibonacci = Fibonacci()
    fib_sum: int = 0
    current_value: int = 0
    while current_value < limit:
        current_value: int = fib.next()
        idx: int = fib.get_current_item()
        if idx < 2:
            print(f'skipped: {idx} = {fib.get_current()}')
            continue
        if Number.is_even(current_value):
            print(f'added: {idx} = {fib.get_current()}')
            fib_sum += current_value
        # else:
        print(f'skipped: {idx} = {fib.get_current()}')
    return fib_sum


print(f'fib: {fibonacci(4000000)}')
