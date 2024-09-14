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
