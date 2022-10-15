message = "GUVF VF ZL FRPERG ZRFFNTR"  #需要破译的密文
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(LETTERS)):
    translated = ''
    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            num = num - key
            if num < 0:
                num += len(LETTERS)
            translated += LETTERS[num]
        else:
            translated += symbol
    print("Key %s : %s"%(key , translated))