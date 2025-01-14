from Crypto.Cipher import AES
from secrets import token_bytes

key = token_bytes(16)

def encrypt(message):
    cipher = AES.new(key , AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(message.encode('ascii'))
    return nonce, ciphertext, tag

def decrypt(nonce,ciphertext,tag):
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)

    try:
        cipher.verify(tag)
        return plaintext.decode('ascii')
    except:
        return False


pt = input("\nEnter plaintext here ->")

nonce, ciphertext, tag = encrypt(pt)
print("\n------------------------------------------------------")
print("\n\t\t\tAES Algorithm")
print("\n------------------------------------------------------")
print(f"The encrypted cipher text of '{pt}' is ->"+str(ciphertext))

plaintext = decrypt(nonce, ciphertext, tag)

if not plaintext:
    print("\nCorrupted message")
else:
    print("\nDecrypted message is ->"+str(plaintext))
