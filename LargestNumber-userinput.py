def get_largest_number(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

numbers = list(map(int, input("Enter a list of numbers, separated by space: ").strip().split()))
print("The largest number is:", get_largest_number(numbers))