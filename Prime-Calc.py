def is_prime(number):
    # Prime numbers are greater than 1
    if number <= 1:
        return False
    
    # Check if the number is divisible by any integer from 2 to the square root of the number
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    
    return True

# Example usage:
num = 980561745
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
