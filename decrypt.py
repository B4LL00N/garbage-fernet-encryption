from cryptography.fernet import Fernet

#Load
with open('key.key', 'rb') as mykey:
    key = mykey.read()
    
    
#Input
bruh = raw_input("Please select a file to decrypt: ")

#Decrypt
f = Fernet(key)

with open(bruh, 'rb') as encrypted_file:
    encrypted = encrypted_file.read()

decrypted = f.decrypt(encrypted)

with open(bruh, 'wb') as decrypted_file:
    decrypted_file.write(decrypted)