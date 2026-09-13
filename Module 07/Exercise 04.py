def sum_list(numbers):
    """Returns the sum of all integers in the list."""
    total = 0
    for n in numbers:
        total += n
    return total


# main program (test)
my_numbers = [4, 8, 15, 16, 23, 42]
result = sum_list(my_numbers)
print(f"The list is: {my_numbers}")
print(f"The sum is: {result}")