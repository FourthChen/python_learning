def main():
    myMessage = "Common sense is not so common."
    myKey = 8

    ciphertext = encryptMessage(myKey, myMessage)

    print(ciphertext + "|")



def encryptMessage(key, message):
    ciphertext = [''] * key

    for col in range(key):
        pointer = col

        while pointer < len(message):
            ciphertext[col] = ciphertext[col] +message[pointer]
            pointer =pointer + key
    return ''.join(ciphertext)#join方法是将列表中的字符串拼接成一个大的字符串


if __name__ == "__main__":
    main()