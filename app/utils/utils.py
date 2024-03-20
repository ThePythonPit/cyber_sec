from cryptography.fernet import Fernet
from flask import redirect, url_for, flash
from flask_login import current_user
from functools import wraps
from flask import flash, redirect, url_for
from flask_login import current_user

def generate_key():
    """
    Generates a secure key.
    Returns:
        A URL-safe base64-encoded 32-byte key. This should be kept secret.
    """
    return Fernet.generate_key()

def encrypt_message(message, key):
    """
    Encrypts a message using the provided key.
    
    Args:
        message (str): The message to encrypt.
        key (bytes): The secret key (must be 32 url-safe base64-encoded bytes).

    Returns:
        bytes: The encrypted message as a byte string.
    """
    cipher_suite = Fernet(key)
    cipher_text = cipher_suite.encrypt(message.encode())
    return cipher_text


def permission_required(permission):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.can(permission):
                flash('You do not have permission to access this page.', 'danger')
                return redirect(url_for('main.home'))  # Reindirizza alla home se non autorizzato
            return f(*args, **kwargs)
        return decorated_function
    return decorator



def permission_required(permission):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.can(permission):
                flash('You do not have permission to access this resource.', 'warning')
                return redirect(url_for('main.home'))
            return f(*args, **kwargs)
        return decorated_function
    return decorator
def decrypt_message(cipher_text, key):
    """
    Decrypts an encrypted message back to its original form using the provided key.
    
    Args:
        cipher_text (bytes): The encrypted message to decrypt.
        key (bytes): The secret key used for encryption (must be 32 url-safe base64-encoded bytes).

    Returns:
        str: The decrypted message.
    """
    cipher_suite = Fernet(key)
    plain_text = cipher_suite.decrypt(cipher_text).decode()
    return plain_text
