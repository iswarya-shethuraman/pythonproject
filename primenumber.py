# Get the maximum number to check for primes
max_num = int(input("Enter a maximum number: "))

# Check each number from 2 to the maximum for primeness
num = 2
while num <= max_num:
    is_prime = True
    divisor = 2
    while divisor <= num / 2:
        if num % divisor == 0:
            is_prime = False
            break
        divisor += 1
    if is_prime:
        print(num)
    num += 1