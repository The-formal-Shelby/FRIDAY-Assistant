# encryption_lib.py
from cryptography.fernet import Fernet, InvalidToken
import base64
import os

def get_key():
    key_path = "secret.key"
    if os.path.exists(key_path):
        with open(key_path, "rb") as key_file:
            return key_file.read()
    else:
        key = Fernet.generate_key()
        with open(key_path, "wb") as key_file:
            key_file.write(key)
        return key

key = get_key()
cipher = Fernet(key)

def encrypt(data: str) -> str:
    """Encrypt sensitive data"""
    if not data:
        return ""
    try:
        return cipher.encrypt(data.encode()).decode()
    except Exception as e:
        print(f"Encryption error: {e}")
        return ""

def decrypt(encrypted_data: str) -> str:
    """Decrypt data"""
    if not encrypted_data:
        return ""
    try:
        return cipher.decrypt(encrypted_data.encode()).decode()
    except InvalidToken:
        print("ERROR: Invalid token - possible key mismatch or corrupted data")
        print("Try deleting secret.key and regenerating your encrypted token")
        return ""
    except Exception as e:
        print(f"Decryption error: {e}")
        return ""

decrypt_key = decrypt  # For compatibility