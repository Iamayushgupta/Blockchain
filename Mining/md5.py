import hashlib 
str = "Ayush Gupta"

result = hashlib.md5(str.encode())
print("The hash value of input string is ",end= " ")
print(result.hexdigest())