import re

def validate_email(email):
    # Regular expression pattern to check the rules
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*(),.?":{}|<>]).+$'

    # Check if email matches the pattern
    if re.match(pattern, email):
        return "Valid email ID"
    else:
        return "Invalid email ID"

# Taking email input from the user
email = input("Enter your email ID: ")
print(validate_email(email))