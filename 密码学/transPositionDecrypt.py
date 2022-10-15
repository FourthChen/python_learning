import math


def main():
    myMessage = "Cenoonommstmme oo snnio. s s c"
    myKey = 8

    ciphertext = decryptMessage(myKey, myMessage)

    print(ciphertext + "|")


def decryptMessage(key, message):
    numOfColumns = int(math.ceil(len(message) / float(key)))#numOfColums为列数，ceil()函数表示向上取整
    numOfRows = key
    numOfShadeBoxes = (numOfColumns * numOfRows) - len(message) #计算网格中灰色格子的个数
    plaintext = [''] * numOfColumns

    col = 0
    row = 0
    for symbol in message:
        plaintext[col] += symbol
        col += 1

        if col == numOfColumns or col == numOfColumns - 1 and row >= numOfRows - numOfShadeBoxes:
            col = 0
            row += 16
    return ''.join(plaintext)


if __name__ == "__main__":
    main()