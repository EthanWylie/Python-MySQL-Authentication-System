import sqlite3
import mysql.connector
import bcrypt

from validation import emailValidation
from encryption import passwordEncryption

dataBase = None
databaseType = None

def connectToDatabase(choice):
    global dataBase
    global databaseType

    if choice == "sqlite":
        databaseType = "sqlite"
        # Create a connection to the SQLite database
        dataBase = sqlite3.connect("encryption_website.db")
        mycursor = dataBase.cursor()
        mycursor.execute("""
            create table if not exists users(
                user_id integer primary key autoincrement,
                user_email text not null unique,
                user_password text not null,
                first_name text,
                last_name text
            )
        """)
        dataBase.commit()

    elif choice == "mysql":
        databaseType = "mysql"
        # Create a connection to the MySQL database
        dataBase = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "Password",
            database = "encryption_website"
            )
    else:
        print("Invalid choice. Please choose either 'sqlite' or 'mysql'.")


def createAccount(emailEntry, passwordEntry):
    # Get users input
    email = emailEntry.get()
    password = passwordEntry.get()

    if len(password) <8:
        print("Passwords has to be at least 8 characters long")
        return
    
    hashed_password = passwordEncryption(password)
    if isinstance(hashed_password, bytes):
        hashed_password = hashed_password.decode('utf-8')

    if emailValidation(email):

        # Use the cursor to execute an SQL query to insert a new record
        mycursor = dataBase.cursor()
        
        try:
            if databaseType == "mysql":
                sql = "INSERT INTO users(user_email, user_password) VALUES (%s, %s)"
            else:
                sql = "INSERT INTO users(user_email, user_password) VALUES (?, ?)"

            val = (email, hashed_password)
            mycursor.execute(sql, val)

            # Commit the changes to the database
            dataBase.commit()

            print("Account created successfully!")

        except (mysql.connector.IntegrityError, sqlite3.IntegrityError):
            print("Email already exists. Please choose a different email.")

        except Exception as err:
            print(f"An error occurred while creating the account: {err}")

    else:
        print("Invalid Email")

def loginHandle(emailEntry, passwordEntry):
    # Get users input
    email = emailEntry.get()
    password = passwordEntry.get()

    # Use the cursor to execute an SQL query to see if the  email and password exist
    mycursor = dataBase.cursor()
    if databaseType == "mysql":
        sql = "SELECT * FROM users WHERE user_email = %s"
    else:
        sql = "SELECT * FROM users WHERE user_email = ?"
    
    # Need comma at the end to make a tuple
    val = (email,)
    mycursor.execute(sql, val)

    result = mycursor.fetchone()

    # If login successful then print success, else print not successful
    if result:
        hashed_password = result[2].encode('utf-8')
        if bcrypt.checkpw(password.encode("utf-8"), hashed_password):
            print("Login successful")
        else:
            print("Login not successful")
    else:
        print("Login not successful")
