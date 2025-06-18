import hashlib
password = "sample123"
user_password = str(input("Enter the password: "))

password_hash = hashlib.sha256(password.encode())
user_password_hash = hashlib.sha256(user_password.encode())

if user_password_hash.hexdigest() == password_hash.hexdigest():
    print("Passwords match! Have same hash values")
else:
    print("Password doesn't match!")    