from cryptography.fernet import Fernet

encryption_key = None

def read_encryption_key():
    global encryption_key
    try:
        with open("encryption.key", "rb") as f:
            encryption_key = f.read()
    except (IOError) as error:
        print(error)


def encrypt_password(password):
    global encryption_key

    if encryption_key == None:
        print("No encryption key detected")
        return -1

    f = Fernet(encryption_key)
    password_encrypted = f.encrypt(password.encode())

    #print(password_encrypted)
    return password_encrypted



def decrypt_password(b_encrypted_password):
    global encryption_key

    if encryption_key == None:
        print("No encryption key detected")
        return -1

    f = Fernet(encryption_key)
    password_decrypted = f.decrypt(b_encrypted_password)

    password_decoded = password_decrypted.decode()

    #print(password_decoded)
    return password_decoded
    

if __name__ == '__main__':

    read_encryption_key()

    password = "yoyomekie123"
    b_enc_pass = encrypt_password(password)


    rec_password = decrypt_password(b_enc_pass)
    print(rec_password)



