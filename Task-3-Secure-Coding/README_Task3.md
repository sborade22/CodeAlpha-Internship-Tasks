# Task 3 – Secure Coding Review

## Project Overview
This project was completed as part of the CodeAlpha Cybersecurity Internship.
It demonstrates a simple Python login system and a basic secure-coding
improvement by comparing a password hash instead of storing the password
as plain text.

## Features
- Accepts a username and password
- Hides password input in the terminal
- Hashes the entered password using SHA-256
- Compares credentials and displays a login result
- Uses a generic error message for invalid credentials

## Demo Credentials
- Username: `admin`
- Password: `admin123`

## Technology Used
- Python 3
- `hashlib`
- `hmac`
- `getpass`

## How to Run
1. Open a terminal in this folder.
2. Run:

   ```bash
   python secure_login.py
   ```

3. Enter the demo credentials to test a successful login.

## Security Note
SHA-256 is included here for educational demonstration and is not suitable
for storing passwords in a production system. Real applications should use
Argon2id or bcrypt with a unique salt, plus controls such as rate limiting
and secure account management.

## Internship
CodeAlpha – Cybersecurity Internship, Task 3: Secure Coding Review.
