import pyperclip

message = "this is my secret message"
key = 13

mode = "encrypt"#加密
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
translated = ''
message = message.upper()  #转换为大写

for symbol in message:
    if symbol in LETTERS:
        num = LETTERS.find(symbol)  #接受一个字符串参数，返回一个整数索引，字符串出现的位置
        if mode == "encrypt":
            num = num + key
        elif mode == "decrypt":
            num = num - key

        if num >= len(LETTERS):
            num = num - len(LETTERS)
        elif num < 0:
            num = num + len(LETTERS)

        translated = translated + LETTERS[num]

    else:
        translated = translated + symbol

print(translated)