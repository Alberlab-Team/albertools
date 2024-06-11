import hashlib
import ssl
import hmac
import base64

# Hash a string using various methods
def hash_string(string: str, method: str) -> str:
    string_bytes = string.encode('utf-8')
    
    if method.lower() == 'md5':
        hash_object = hashlib.md5(string_bytes)
    elif method.lower() == 'sha1':
        hash_object = hashlib.sha1(string_bytes)
    elif method.lower() == 'sha256':
        hash_object = hashlib.sha256(string_bytes)
    elif method.lower() == 'sha512':
        hash_object = hashlib.sha512(string_bytes)
    else:
        raise ValueError("Unsupported hash method.")
    return hash_object.hexdigest()

# Check if SSL/TLS is available
def is_ssl_available():
    return ssl.OPENSSL_VERSION

# Generate a message authentication code (MAC) using HMAC
def generate_mac(key: str, message: str) -> str:
    key_bytes = key.encode()
    message_bytes = message.encode()
    mac = hmac.new(key_bytes, message_bytes, hashlib.sha256)
    return mac.hexdigest()

# Encode a string using Base64
def encode_base64(string: str) -> str:
    return base64.b64encode(string.encode()).decode()

# Decode a Base64-encoded string
def decode_base64(encoded_string: str) -> str:
    return base64.b64decode(encoded_string).decode()

# Encrypt a string using a simple Caesar cipher
def caesar_cipher_encrypt(string: str, shift: int) -> str:
    result = ""
    for char in string:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            result += chr(shifted)
        else:
            result += char
    return result

# Decrypt a string encrypted with a Caesar cipher
def caesar_cipher_decrypt(string: str, shift: int) -> str:
    return caesar_cipher_encrypt(string, -shift)