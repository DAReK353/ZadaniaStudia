def encryption(encdec, number, sampletext):
    if encdec == 2:
        number = number * -1
    readytext = ""
    for i in sampletext:
        letter = ord(i)
        letter += number
        readytext += chr(letter)
    return readytext


def encryptionfile(encdec, number, sampletext):
    if encdec == 3:
        file2 = open("Encrypted" + sampletext, "w+")
    else:
        number = number * -1
        file2 = open("Decrypted" + sampletext, "w+")
    file = open(sampletext, "r+")
    for line in file:
        readytext = ""
        line = line.strip()
        for x in line:
            letter = ord(x)
            letter += number
            readytext += chr(letter)
        file2.write(readytext + "\n")
    file.close()
    file2.close()


while True:
    print("Do you want to Encrypt or Decrypt?")
    print("1. Encrypt Text")
    print("2. Decrypt Text")
    print("3. Encrypt File")
    print("4. Decrypt File")
    print("5. Exit")
    userchoice = int(input())

    if userchoice == 1 or userchoice == 2:
        print("What do you want to encrypt/decrypt: ")
    elif userchoice == 3 or userchoice == 4:
        print("Enter the name of the file you want to encrypt/decrypt: ")
    text = input()

    encryptionumber = input("What encryption / decryption number do you want?: ")
    encryptionumber = int(encryptionumber)

    if userchoice == 1 or userchoice == 2:
        print("The result:", encryption(userchoice, encryptionumber, text))
    elif userchoice == 3 or userchoice == 4:
        encryptionfile(userchoice, encryptionumber, text)
        print("Encrypted / Decrypted successfully.")
    elif userchoice == 5:
        exit()
