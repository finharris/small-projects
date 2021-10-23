import hashlib


def hasher(passw):
    hashed = hashlib.md5(passw)
    return hashed.hexdigest()


tobehashed = input("What would you like to be hashed with md5? ").encode("utf-8")

print(hasher(tobehashed))
