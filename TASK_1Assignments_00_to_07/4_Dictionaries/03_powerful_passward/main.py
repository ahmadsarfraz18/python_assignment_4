
from hashlib import sha256

def hash_password(password):

    """Takes a password and hashes it using sha256"""
    
    return sha256(password.encode()).hexdigest()
def login(email, stored_logins, password_to_check):

    """ Returns True if the password we are checking matches the one in stored_logins
     for a specific email. Otherwise returns False """
    
    return stored_logins.get(email) == hash_password(password_to_check)

def main():
    stored_logins = {
        'LXO7c@example.com': 'c0f1c1e9d0d1c1e9d0d1c1e9d0d1c1e9d0d1c1e9d0d1c1e9d0d1c1e9d0d1c1e9',
        't3LXO7c@example.com': 'c0f1c1e9d0d1c1e9d0d1c1e9d0d1c1e9d0d1c1e9d0d1c1e9d0d1c1e9d0d1c1e9',
        'X0m8w@example.com': 'c0f1c1e9d0d1c1e9d0d1c1e9d0d1c1e9d0d1c1e9d0d1c1e9d0d1c1e9d0d1c1e9',
    }

    email = input('Enter your email: ')
    password = input('Enter your password: ')

    if login(email, stored_logins, password):
        print('Login successfully')
    else:
        print('Login failed. Invalid email or password')

if __name__ == "__main__":
    main()
    