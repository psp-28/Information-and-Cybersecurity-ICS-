from Crypto.Cipher import DES                   # install package crypto and rename package in C drive folder as Crypto and install pycryptodome package is new one
from secrets import token_bytes

key = token_bytes(8)

def encrypt(message):
    cipher = DES.new(key, DES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag =cipher.encrypt_and_digest(message.encode('ascii'))
    return nonce,ciphertext, tag

def decrypt(nonce, ciphertext, tag):
    cipher = DES.new(key, DES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)

    try:
        cipher.verify(tag)
        return plaintext.decode('ascii')
    except:
        return False


pt = input("Enter the plain text ->")

nonce, ciphertext, tag = encrypt(pt)
print("\n-------------------------------------------------------------")
print("\n\t\t\t\tDES Algorithm")
print("\n-------------------------------------------------------------")
print(f"\n The Encrypted ciphertext of'{pt}' is ->",ciphertext)

plaintext =decrypt(nonce, ciphertext, tag)

if not plaintext:
    print("\nCorrupted message")
else:
    print("The plaintext is decrypted is ->"+str(plaintext))