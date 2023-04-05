import binascii
import hashlib
# Convert raw_block from hex string to binary format
binary_block = binascii.unhexlify("0010000009e973a3b68a1a9618c7a4d0db9c4e2b08983b24c6d77f43d4ecb407a0000000088e7d8a6de1e3c3bda5df7c5a5f0d5e6051a6ca2eb85d9e9c23b2f1b17732f2e3b50a88ac1e0118e2330700119821")

# Extract block header
block_header = binary_block[:80]

# Parse block header to extract information
block_version = block_header[:4]
prev_block_hash = block_header[4:36]
merkle_root = block_header[36:68]
timestamp = block_header[68:72]
bits = block_header[72:76]
nonce = block_header[76:80]

# Extract transactions
transactions = binary_block[80:]

# Initialize transaction count
transaction_count = 0

# Loop through transactions and extract information
while transactions:
    # Increment transaction count
    transaction_count += 1
    
    # Extract transaction details
    version = transactions[:4]
    input_count = int.from_bytes(transactions[4:5], byteorder='little')
    inputs = transactions[5:5+input_count*41]  # Each input is 41 bytes
    output_count = int.from_bytes(transactions[5+input_count*41:5+input_count*41+1], byteorder='little')
    outputs = transactions[5+input_count*41+1:5+input_count*41+1+output_count*31]  # Each output is 31 bytes
    locktime = transactions[-4:]
    
    # Calculate transaction hash (little-endian)
    transaction_hash = binascii.hexlify(hashlib.sha256(hashlib.sha256(transactions[:4+5+input_count*41+1+output_count*31+4]).digest()).digest()[::-1]).decode()
    
    # Convert extracted binary data to little-endian hex strings
    version_hex = binascii.hexlify(version[::-1]).decode()
    locktime_hex = binascii.hexlify(locktime[::-1]).decode()
    
    # Print extracted information
    print("Transaction No.", transaction_count)
    print("Transaction Hash:", transaction_hash)
    print("Version:", int(version_hex, 16))
    print("Number of Inputs:", input_count)
    print("Number of Outputs:", output_count)
    print("Locktime:", int(locktime_hex, 16))
    print()
    
    # Move to the next transaction
    transactions = transactions[4+5+input_count*41+1+output_count*31:]
