# Ask the user for their username
# Then ask for their password
# If the user’s username is robert and their password is password123, print your deepest, darkest secret. 
# If not, tell the user to get lost

USERNAME1 = 'robert'
PASSWORD1 = 'password123'

"""users = {
    "user1":{
    "username": USERNAME1,
    "password": PASSWORD1,
    },
    "user2": {
    "username": "anoosh",
    "password": "snuffles456",
    },
    "user3": {
    "username": "kira",
    "password": "jotaro228",
    }

}"""

users = [
  {
    'username': 'robert',
    'password': 'password123'
  },
  {
    'username': 'anoosh',
    'password': 'snuffles456'
  },
 {
    'username': 'juan',
    'password': 'happyland'
  }
]

def is_valid_credentials(username: str, password: str):
    # For List that contains dictionaies
    for user in users:
        if username == user.get("username") and password == user["password"]:
            return True # Match Found
    return False # No match found

    """ For Dictionary of users
    for user in users.values():
        if username == user.get("username") and password == user["password"]:
            return True # Match Found
    return False # No match found
    """

def main():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if is_valid_credentials(username, password):
        print("Welcome, you've unlocked my deepest, darkest secret!")
        return f"My secret is: I am secretly a Python enthusiast."
    else:
        return f"Incorrect username or password. Get lost!"

if __name__ == "__main__":
    print(main())

 
