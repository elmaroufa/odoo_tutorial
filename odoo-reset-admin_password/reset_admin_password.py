from passlib.context import CryptContext

# Define the password hashing context
pwd_context = CryptContext(
    schemes=["pbkdf2_sha512"],  
    pbkdf2_sha512__rounds=600000  # Set the number of rounds (iterations)
)

# Function to hash the password
def encrypt_password(password):
    return pwd_context.hash(password)

# Prompt the user to enter their password
user_password = input("Enter your password: ")

# Encrypt the password and display it
encrypted_password = encrypt_password(user_password)
print(f"Encrypted password: {encrypted_password}")
