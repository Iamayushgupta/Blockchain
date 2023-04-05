import binascii

# Convert raw_block from hex string to binary format
binary_block = binascii.unhexlify("0010000009e973a3b68a1a9618c7a4d0db9c4e2b08983b24c6d77f43d4ecb407a0000000088e7d8a6de1e3c3bda5df7c5a5f0d5e6051a6ca2eb85d9e9c23b2f1b17732f2e3b50a88ac1e0118e2330700")

# Extract block header
block_header = binary_block[:80]

# Parse block header to extract information
block_version = block_header[:4]
prev_block_hash = block_header[4:36]
merkle_root = block_header[36:68]
timestamp = block_header[68:72]
bits = block_header[72:76]
nonce = block_header[76:80]

# Convert extracted binary data to little-endian hex strings
block_version_hex = binascii.hexlify(block_version[::-1]).decode()
prev_block_hash_hex = binascii.hexlify(prev_block_hash[::-1]).decode()
merkle_root_hex = binascii.hexlify(merkle_root[::-1]).decode()
timestamp_hex = binascii.hexlify(timestamp[::-1]).decode()
bits_hex = binascii.hexlify(bits[::-1]).decode()
nonce_hex = binascii.hexlify(nonce[::-1]).decode()

# Print extracted information
print("Block Version:", int(block_version_hex, 16))
print("Previous Block Hash:", prev_block_hash_hex)
print("Merkle Root:", merkle_root_hex)
print("Timestamp:", int(timestamp_hex, 16))
print("Bits:", bits_hex)
print("Nonce:", nonce_hex)
