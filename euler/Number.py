class Number:

    @classmethod
    def is_even(cls, number: int) -> bool:
        return number % 2 == 0

    @classmethod
    def is_odd(cls, number: int) -> bool:
        return not cls.is_even(number)

    @classmethod
    def is_multiplication_of_any_factor(cls, factors: list[int], checked_number: int):
        if checked_number is None:
            raise TypeError("The checked_number can't be null")
        if factors is None:
            raise TypeError("The factors can't be null")

        multiplications: list[int] = []
        for current_factor in factors:
            is_multiplication: bool = checked_number % current_factor == 0
            if is_multiplication:
                multiplications.append(current_factor)
        return multiplications
