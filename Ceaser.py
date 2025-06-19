def ceaser_encrypt(text,key):
    result=""
    for char in text:
        if char.isalpha():
            shift=key%26
            base=ord('A') if char.isupper() else ord('a')
            result+=chr((ord(char)-base+shift)%26 +base)
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
    print("\n 1.Encryption \n 2.Decryption \n")
    choice=input("Enter your choice(1/2):")

    if choice=='1':
        key=int(input("Enter key:"))
        plaintext=read_file("input.txt")
        encrypted=ceaser_encrypt(plaintext,key)
        write_file("encrypted.txt",encrypted)
        print("Encrypted text saved to encrypted.txt")

    elif choice=='2':
        key=int(input("Enter the key used during encrption:"))
        ciphertext=read_file("encrypted.txt")
        decrypted=ceaser_encrypt(ciphertext,-key)
        write_file("decrypted.txt",decrypted)
        print("Decrypted text is saved to decrypted.txt")

    else:
        print("Invalid choice.")
if __name__=="__main__":
    while True:
        main()