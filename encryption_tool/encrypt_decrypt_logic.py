from cryptography.fernet import Fernet


def generate_key():
    key = Fernet.generate_key()
    return key

def encrypt_file(file, key):
    f = Fernet(key)
    encrypted_data = f.encrypt(file.read())
    return encrypted_data

def decrypt_file(encrypted_data, key):
    f = Fernet(key)
    return f.decrypt(encrypted_data)




