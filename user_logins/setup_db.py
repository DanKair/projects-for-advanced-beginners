import sqlite3 , os, json

current_dir = os.getcwd()
if current_dir != os.path.join(current_dir, "user_logins"):
    os.chdir("user_logins")
    print(f"Changed to the {os.getcwd()}")

# Load JSON data from file
with open('credentials.json', 'r') as file:
    credentials = json.load(file)  # This becomes a list of dictionaries
    

# Connecting to database and initialize cursor for SQL Queries
connection = sqlite3.connect('ppab6-test.db')
cursor = connection.cursor()

# Create Table Users
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
username TEXT NOT NULL,
password_hash TEXT NOT NULL
)
''')


# Insert values into 2 columns
for user in credentials:
    cursor.execute('''
    INSERT INTO Users (username, password_hash) VALUES (?, ?)
    ''', (user["username"], user["password_hash"]))

# Commit changes and close connection
connection.commit()
connection.close()

