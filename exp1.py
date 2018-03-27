import hashlib 
msg  = hashlib.md5(b"SALUT).digest()
def hash(msg):
    return hashlib.md5(msg.encode()).digest()
print(msg)
print (hash(b" bonjour les collégues"))
