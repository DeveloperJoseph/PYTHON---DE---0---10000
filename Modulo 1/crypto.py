import hashlib

crypt = hashlib.sha256()
crypt.update(b"hello")#b reference to bytes
print(crypt.hexdigest())