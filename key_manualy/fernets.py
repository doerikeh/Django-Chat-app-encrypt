import cryptography
from cryptography.fernet import Fernet

file = open('key.key', 'rb')
key = file.read()
file.close()

#  Open the file to decrypt
with open('contoh.txt.decrypted', 'rb') as f:
    data = f.read()

fernet = Fernet(key)
encrypted = fernet.decrypt(data)

# Open the decrypted file
with open('contoh.txt.decrypted', 'wb') as f:
    f.write(encrypted)