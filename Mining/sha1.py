import hashlib
str = "Ayush Gupta"
# result = hashlib.sha256(str.encode())
# print("The hexadecimal equivalent of SHA256 is : ",end="")
# print(result.hexdigest())

# result = hashlib.sha384(str.encode())
# print("The hexadecimal equivalent of SHA384 is : ",end="")
# print(result.hexdigest())

# result = hashlib.sha224(str.encode())
# print("The hexadecimal equivalent of SHA224 is : ",end="")
# print(result.hexdigest())

# result = hashlib.sha512(str.encode())
# print("The hexadecimal equivalent of SHA512 is : ",end="")
# print(result.hexdigest())
result = hashlib.sha1(str.encode())

print("The hexadecimal equivalent of SHA1 is : ",end="")
print(result.hexdigest())

