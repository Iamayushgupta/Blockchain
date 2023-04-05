import hashlib

str = "Ayush Gupta"
result = hashlib.sha256(str.encode())

print("The hexadecimal equivalent of SHA256 is : ",result.hexdigest())