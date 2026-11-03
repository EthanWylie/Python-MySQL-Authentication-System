# Encryption System

Welcome to the Password Encryption GUI, a Python application for user authentication and password encryption using bcrypt. This project provides a simple environment for account creation and login, with the option to use either SQLite or MySQL as the database.

## Description

This GUI application allows users to register accounts with hashed passwords using bcrypt. Users can choose between SQLite and MySQL when launching the application.

SQLite automatically creates a local database, making it easier to get started without installing a database server. MySQL is also supported for users who prefer to use their own MySQL server.

The application also includes email validation and password verification for account authentication.

## Features
- User registration with email validation
- Password hashing using bcrypt
- User login with password verification
- SQLite database integration
- MySQL database integration
- Database selection when launching the application
- Automatic SQLite database and table creation
- Unique email addresses for user accounts

## Prerequisites
- Python 3.11.2 or newer
- Required Python packages:
- customtkinter
- mysql-connector-python
- bcrypt

## Setup
1. Clone the repository:
git clone https://github.com/EthanWylie/Python-MySQL-Authentication-System
cd Python-MySQL-Authentication-System

2. Install dependencies:
pip install -r requirements.txt

3. Run the application:
python pythonFiles/main.py

## Database Setup

When launching the application, you can choose between SQLite and MySQL.

### SQLite
* Select sqlite from the database selection menu.
* Click Continue.
* The application automatically creates the encryption_website.db database and the required users table.
* No additional database setup is required.
### MySQL
* Install MySQL Server and make sure it is running.
* Open setup.sql in MySQL Workbench and execute the script to create the encryption_website database and users table.
* Update the MySQL connection details in database.py to match your MySQL configuration.
* Select mysql from the database selection menu.
* Click Continue.
### Usage
* Launch the application.
* Choose between SQLite and MySQL.
* Click Continue to connect to your selected database.
* Use the "Create Account" button to register a new user.
* Enter a valid email and a password with at least 8 characters.
* Use the "Login" button to log in with an existing account.
### Technologies Used
* Python
* CustomTkinter
* SQLite
* MySQL
* bcrypt
