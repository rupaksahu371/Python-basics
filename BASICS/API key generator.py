import secrets
import string

def generate_api_key(length=24):
    # Define the character set: uppercase, lowercase letters and digits
    alphabet = string.ascii_letters + string.digits
    # Generate a random API key of the specified length
    return ''.join(secrets.choice(alphabet) for _ in range(length))

# Generate and print a 24-character API key
api_key = generate_api_key(24)
print("Generated API Key:", api_key)   