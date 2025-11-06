from cryptography.fernet import Fernet

# 키 생성
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# 암호화
text = b"Hello, cryptography!"
cipher_text = cipher_suite.encrypt(text)
print(f"Cipher Text: {cipher_text}")

# 복호화
decrypted_text = cipher_suite.decrypt(cipher_text)
print(f"Decrypted Text: {decrypted_text}")