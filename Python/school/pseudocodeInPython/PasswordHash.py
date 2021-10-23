import hashlib

def hash(v):
  return hashlib.sha256(bytes(v, encoding='utf-8')).hexdigest()

hashed = '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8' # password

password = input('enter password ')

if hash(password) == hashed:
  print(True)
else:
  print(False)