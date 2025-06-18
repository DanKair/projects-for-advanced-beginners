import hashlib, os
from dotenv import load_dotenv

load_dotenv()

PASSWORD1 = os.getenv("PASSWORD1")
PASSWORD2 = os.getenv("PASSWORD2")
PASSWORD3 = os.getenv("PASSWORD3")


users = [
  {
    'username': 'robert',
    'password': hashlib.sha256(PASSWORD1.encode()).hexdigest(),
  },
  {
    'username': 'anoosh',
    'password': hashlib.sha256(PASSWORD2.encode()).hexdigest(),
  },
  {
    'username': 'juan',
    'password': hashlib.sha256(PASSWORD3.encode()).hexdigest(),
  }
]

def is_valid_credentials(username: str, password: str):
    hashed_password = hashlib.sha256(password.encode())
    # For List that contains dictionaies
    for user in users:
        if username == user.get("username") and hashed_password.hexdigest() == user["password"]:
            # print(f"Hash of the password: {user['password']}") # uncomment this if you wanna check the hash value of the password
            return True # Match Found
    return False # No match found


def main():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if is_valid_credentials(username, password):
        print(f"Welcome {username}, you've unlocked my deepest, darkest secret!")
        return f"My secret is: I have been in Tutorial Hell for a long time."
    else:
        return f"Incorrect username or password. Get lost!"

if __name__ == "__main__":
    print(main())

 
