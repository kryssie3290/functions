def count_even(numbers):
    count = 0
    for num in numbers:
        if num % 2 == 0:
           count += 1
    return count
print(count_even([1, 2, 3, 4, 5, 6,]))
