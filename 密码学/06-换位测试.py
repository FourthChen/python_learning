import os
from 密码学 import transPositionEncrypt

from 密码学 import transPositionDecrypt

import random
import sys
def main():
    random.seed(42)
    for i in range(20):
        message = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" * random.randint(4, 40)
        message = list(message)
        random.shuffle(message)
        message = ''.join(message)
        print("Test #%s : %s..." % (i + 1, message[:50]))

        for key in range(1, len(message)):
            encrypted= transPositionEecrypt.encryptMessage(key,message)
            decrypted= transPositionDecrypt.decryptMessage(key,encrypted)
            if message != decrypted:
                print("Mismatch with key %s and message %s." % (key, message))
                print(decrypted)
                sys.exit()
    print("Transposition cipher test passed.")


if __name__ == "__main__":
    main()