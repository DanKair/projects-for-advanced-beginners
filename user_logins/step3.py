import json, hashlib, os

# 0. Make sure that file's path is relative to your current file path
current_dir = os.getcwd()
if current_dir != os.path.join(current_dir, "user_logins"):
    os.chdir("user_logins")
    print(f"Changed to the {os.getcwd()}")

# 1. Open a json file
# 2. convert json file to python object (dict) and assign it to some variable
# 3. iterate over the dictionary
# 4. get neccessary fields
"""with open("credentials.json", "r") as f:
        credentials = json.load(f)
        for credential in credentials:
            password = credential["password_hash"]
            print(f"Password hash: {password}")
            """

def is_valid_credentials(username: str, password: str):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    # For List that contains dictionaies
    with open("credentials.json", "r") as f:
        credentials = json.load(f)
        for credential in credentials:
            password = credential["password_hash"]
            print(f"Your Password hash: {hashed_password}")
            #print(f"Expected Password hash: {password}")
            if username == credential.get("username") and hashed_password == credential["password_hash"]:

                return True # Match Found
        return False # No match found


def main():
    username = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()

    if is_valid_credentials(username, password):
        print(f"Welcome {username}, you've unlocked my deepest, darkest secret!")
        return f"My secret is: I have been a Vibe Coder in the past."
    else:
        return f"Incorrect username or password. Get lost!"

if __name__ == "__main__":
    print(main())

 
