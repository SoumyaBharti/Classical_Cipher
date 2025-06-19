def encryption(text,key):
    result=""
    key=key.upper()
    key_index=0

    for char in text:
        if char.isalpha():
            shift=ord(key[key_index % len(key)])-ord('A')
            base=ord('A') if char.isupper() else ord('a')
            result+=chr((ord(char)-base+shift)%26+base)
            key_index+=1
        else:
            result+=char
    return result

def decryption(text,key):
    result=""
    key=key.upper()
    key_index=0

    for char in text:
        if char.isalpha():
            shift=ord(key[key_index % len(key)])-ord('A')
            base=ord('A') if char.isupper() else ord('a')
            result+=chr((ord(char)-base-shift+26)%26+base)
            key_index+=1
        else:
            result+=char
    return result

def read_file(filename):
    with open(filename,"r") as file:
        return file.read()

def write_file(filename,content):
    with open(filename,"w") as file:
        file.write(content)

def main():
    print("\n1.Encryption\n2.Decryption")
    choice=input("Enter your choice(1/2):")

    if choice=='1':
        key=input("Enter the keyword:")
        plaintext=read_file("input.txt")
        encrypted=encryption(plaintext,key)
        print("saving to xyz.txt")
        write_file("encrypted.txt",encrypted)
        print("Encrypted text is saved to encrypted.txt")

    elif choice=='2':
        key=input("Enter the keyword:")
        ciphertext=read_file("encrypted.txt")
        decrypted=decryption(ciphertext,key)
        write_file("decrypted.txt",decrypted)
        print("Decrypted text is saved to decrypted.txt")

    else:
        print("Invalid choice")

if __name__=="__main__":
    while True:
        main()