from cryptography.fernet import Fernet

if __name__ == '__main__':
    encryption_key_created = Fernet.generate_key()

    with open("encryption.key", "wb") as f:
        f.write(encryption_key_created)
    
