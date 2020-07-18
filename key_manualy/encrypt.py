from cryptography.fernet import Fernet

file = open('key.key', 'rb')
key = file.read()
file.close()

#  Open the file to encrypt
with open('contoh.txt', 'rb') as f:
    data = f.read()

fernet = Fernet(key)
encrypted = fernet.encrypt(data)

# Write the encrypted file
with open('contoh.txt.encrypted', 'wb') as f:
    f.write(encrypted)