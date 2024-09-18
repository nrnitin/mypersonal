print ("hello")
x=2
y=3
z=x+y
print (z)
def is_palindrome(s):
    # Remove spaces and convert to lowercase for uniform comparison
    cleaned_str = ''.join(c.lower() for c in s if c.isalnum())
    # Compare the cleaned string with its reverse
    return cleaned_str == cleaned_str[::-1]

# Example usage
test_string = input("Enter a string to check if it's a palindrome: ")
if is_palindrome(test_string):
    print(f"'{test_string}' is a palindrome.")
else:
    print(f"'{test_string}' is not a palindrome.")
def is_prime(n):
    """Check if a number is a prime number."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def sum_of_two_digit_primes():
    """Calculate the sum of all two-digit prime numbers."""
    total_sum = 0
    for number in range(10, 100):
        if is_prime(number):
            total_sum += number
    return total_sum

# Calculate and print the sum
result = sum_of_two_digit_primes()
print(f"The sum of all two-digit prime numbers is: {result}")
