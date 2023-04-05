# Using ripemd160 for rehashing/double hashing
import hashlib
ripe = hashlib.new('ripemd160')


# Updating value of hash of output of SHA1 with input of "Ayush Gupta"
ripe.update(b"d7f415fa7cf218c48875cc8fe9360bc070d7ccd1")
print("The hexadecimal equivalent of hash of SHA1 is :", ripe.hexdigest())

# Updating value of hash of output of SHA256 with input of "Ayush Gupta"
ripe.update(b"040178247d770418a82066a6baa17bf2e31f80bcc72ed9236b9bd4e127990e5c")
print("The hexadecimal equivalent of hash of SHA256 is :",ripe.hexdigest())

# Updating value of hash of output of MD5 with input of "Ayush Gupta"
ripe.update(b"cb3d895c5f394f9d7a9ea143e13efcf6")
print("The hexadecimal equivalent of hash of md5 is :",ripe.hexdigest())
