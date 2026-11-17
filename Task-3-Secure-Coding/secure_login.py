"""
CodeAlpha Internship – Task 3: Secure Coding Review
Simple Login System (demonstration)

Demo credentials:
    Username: admin
    Password: admin123

Note: SHA-256 is used here to demonstrate password hashing for the task.
For real applications, use a password-hashing algorithm designed for passwords,
such as Argon2id or bcrypt, with a unique salt.
"""

import hashlib
import hmac
import getpass

USERNAME = "admin"
STORED_PASSWORD_HASH = "240be518fabd2724ddb6f04eeb1da5967448d7e831c08c8fa822809f74c720a9"


def hash_password(password: str) -> str:
    """Return the SHA-256 hash of the supplied password."""
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def login() -> bool:
    print("=" * 45)
    print("       CODEALPHA - SECURE LOGIN SYSTEM")
    print("=" * 45)

    entered_username = input("Enter username: ").strip()
    entered_password = getpass.getpass("Enter password: ")

    entered_password_hash = hash_password(entered_password)

    username_valid = hmac.compare_digest(entered_username, USERNAME)
    password_valid = hmac.compare_digest(
        entered_password_hash, STORED_PASSWORD_HASH
    )

    if username_valid and password_valid:
        print("\nLogin Successful!")
        return True

    print("\nInvalid Username or Password!")
    return False


if __name__ == "__main__":
    login()
