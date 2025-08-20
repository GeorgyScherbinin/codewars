# https://www.codewars.com/kata/558fc85d8fd1938afb000014/train/python
# def sum_two_smallest_numbers(numbers):
#     min1 = min(numbers)
#     numbers.remove(min1)
#     min2 = min(numbers)

#     return (min1 + min2)

def sum_two_smallest_numbers(numbers):
    min1 = min(numbers)
    numbers.pop(numbers.index(min1))
    min2 = min(numbers)

    return (min1 + min2)

print(sum_two_smallest_numbers([10, 343445353, 3453445, 3453545353453]))