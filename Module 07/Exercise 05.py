def remove_odd_numbers(numbers):
    """Returns a new list containing only the even numbers from 'numbers'."""
    even_numbers = []
    for n in numbers:
        if n % 2 == 0:
            even_numbers.append(n)
    return even_numbers


# main program (test)
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cut_down_list = remove_odd_numbers(original_list)

print(f"Original list: {original_list}")
print(f"Cut-down list: {cut_down_list}")