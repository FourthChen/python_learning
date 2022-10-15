# -*-coding:utf-8-*-
UPPERLETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LETTERS_AND_SPACE = UPPERLETTERS + UPPERLETTERS.lower() + ' \t\n'


def loadDictionary():  # 返回一个dict。其中包含了dictionary.txt 中的所有单词
    dictionaryFile = open("dictionary.txt")
    englishWords = {}
    for word in dictionaryFile.read().split('\n'):
        englishWords[word] = None
    dictionaryFile.close()
    return englishWords


ENGLISH_WORDS = loadDictionary()


def removeNonLetters(message):  # 只保留原字符串中的英文和空格部分
    lettersOnly = []
    for symbol in message:
        if symbol in LETTERS_AND_SPACE:
            lettersOnly.append(symbol)
    return ''.join(lettersOnly)


def getEnglishcount(message):  # 返回一个占比值。即这个message中的英文单词占(百分)比多少
    message = message.upper()
    message = removeNonLetters(message)
    possibleWords = message.split()  # 预处理。得到原message中所有单词组成的列表

    if possibleWords == []:
        return 0.0

    matches = 0
    for word in possibleWords:
        if word in ENGLISH_WORDS:
            matches += 1
    return float(matches) / len(possibleWords)


def isEnglish(message, wordPercentage=20, letterPercentage=85):
    wordsMatch = getEnglishcount(message) * 100 >= wordPercentage
    numLetters = len(removeNonLetters(message))
    messageLettersPercentage = float(numLetters) / len(message) * 100
    lettersMatch = messageLettersPercentage >= letterPercentage
    return wordsMatch and lettersMatch