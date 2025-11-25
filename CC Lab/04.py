#Create a Python script to encrypt and decrypt text data using
#symmetric(AES)and asymmetric(RSA)encryption techniques

#Part 1 AES Encrypt+Dycipt
from cryptography.fernet import Fernet

# ---------------- GENERATE AES KEY ----------------
def generate_aes_key():
    key = Fernet.generate_key()
    print("AES Key:", key.decode())
    return key

# ---------------- AES ENCRYPTION ----------------
def aes_encrypt(key, message):
    f = Fernet(key)
    encrypted = f.encrypt(message.encode())
    return encrypted

# ---------------- AES DECRYPTION ----------------
def aes_decrypt(key, encrypted_message):
    f = Fernet(key)
    decrypted = f.decrypt(encrypted_message).decode()
    return decrypted


# Testing AES encryption/decryption
if __name__ == "__main__":
    print("\n--- AES Encryption/Decryption ---")
    aes_key = generate_aes_key()

    message = "Hello Shyam! This is AES encryption."
    encrypted_text = aes_encrypt(aes_key, message)
    decrypted_text = aes_decrypt(aes_key, encrypted_text)

    print("Original:", message)
    print("Encrypted:", encrypted_text)
    print("Decrypted:", decrypted_text)
    
    
#Rsa     
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes


# ---------------- RSA KEY GENERATION ----------------
def generate_rsa_keys():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()

    print("RSA Keys generated successfully.")
    return private_key, public_key


# ---------------- RSA ENCRYPT ----------------
def rsa_encrypt(public_key, message):
    encrypted = public_key.encrypt(
        message.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return encrypted


# ---------------- RSA DECRYPT ----------------
def rsa_decrypt(private_key, encrypted_message):
    decrypted = private_key.decrypt(
        encrypted_message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return decrypted.decode()


# Test RSA encryption/decryption
if __name__ == "__main__":
    print("\n--- RSA Encryption/Decryption ---")
    private_key, public_key = generate_rsa_keys()

    message = "Hello Shyam! This is RSA encryption."
    encrypted_text = rsa_encrypt(public_key, message)
    decrypted_text = rsa_decrypt(private_key, encrypted_text)

    print("Original:", message)
    print("Encrypted:", encrypted_text)
    print("Decrypted:", decrypted_text)
