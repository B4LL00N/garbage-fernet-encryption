#Import
from cryptography.fernet import Fernet

#Generate
key = Fernet.generate_key()

with open('key.key', 'wb') as mykey:
    mykey.write(key)
    
#Load
with open('key.key', 'rb') as mykey:
    key = mykey.read()
#Path
path = raw_input("Please pick file to encrypt: ")
 
#Encrypt
f = Fernet(key)

with open(path, 'rb') as original_file:
    original = original_file.read()

encrypted = f.encrypt(original)

with open (path, 'wb') as encrypted_file:
    encrypted_file.write(encrypted)