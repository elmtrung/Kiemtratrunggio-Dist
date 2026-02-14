
import os
import json
from pathlib import Path
from cryptography.fernet import Fernet

# Hardcoded key for "obfuscation" (not true security against reverse engineering, but stops casual reading)
# Generated using Fernet.generate_key()
_SECRET_KEY = b'gJ2wX9qP4z7yA8bC3dE5fG6hI7jK8lM9nO0pQ1rS2tU='

def get_cipher():
    return Fernet(_SECRET_KEY)

def encrypt_config(config_dict, output_path):
    """Encrypts a dictionary to a file."""
    cipher = get_cipher()
    json_data = json.dumps(config_dict).encode('utf-8')
    encrypted_data = cipher.encrypt(json_data)
    
    with open(output_path, 'wb') as f:
        f.write(encrypted_data)

def decrypt_config(input_path):
    """Decrypts a file to a dictionary."""
    if not os.path.exists(input_path):
        return {}
        
    try:
        cipher = get_cipher()
        with open(input_path, 'rb') as f:
            encrypted_data = f.read()
            
        decrypted_data = cipher.decrypt(encrypted_data)
        return json.loads(decrypted_data.decode('utf-8'))
    except Exception as e:
        print(f"Error decrypting config: {e}")
        return {}
