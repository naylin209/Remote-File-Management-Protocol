from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
import os

#The Encryption Key
key = os.urandom(16)

#Initialization Vector
iv = os.urandom(16)

#The message to be encrypted
message = b"Pakkam Pakka Naynay"
print(f"Message to be encrypted: {message.decode()}\n")

#Encryption
cipher = AES.new(key, AES.MODE_CBC, iv) #Cipher object in CBC mode
ciphertext = cipher.encrypt(pad(message, AES.block_size))

#Decryption
cipher = AES.new(key, AES.MODE_CBC, iv) #Cipher object in CBC mode
plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)

print(f"Encrypted Message: {ciphertext}\n")
print(f"Decrypted Message: {plaintext.decode()}")