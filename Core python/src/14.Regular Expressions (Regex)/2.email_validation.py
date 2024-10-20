import re

def validate_email(email):
    # Regex pattern for email validation
    email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$'
    
    # Use re.match to check if the email matches the pattern
    if re.match(email_pattern, email):
        return True
    else:
        return False

# Example usage:
email = "test.email@example.com"
print(validate_email(email))  # Output: True
