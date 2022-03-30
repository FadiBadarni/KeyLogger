from cryptography.fernet import Fernet

key = "CGSGT35QoI3usquQLXu8z9_Eo1BTABAuHjlIyxNu-_8="

keyboard_info = "e_keyboard.txt"

encrypted_files = [keyboard_info]
count = 0

for decrypting_file in encrypted_files:
    with open(encrypted_files[count], 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    decrypted = fernet.decrypt(data)

    with open(encrypted_files[count],'wb') as f:
        f.write(decrypted)

    count += 1