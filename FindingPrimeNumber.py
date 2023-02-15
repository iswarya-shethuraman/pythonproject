max_num = int(input("Enter a maximum number: "))

# Check each number from 2 to the maximum for primeness
for num in range(1, max_num+1):
    is_prime = True
    for i in range(2, int(num/2)+1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, "is prime")