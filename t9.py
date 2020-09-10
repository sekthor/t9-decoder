#!/usr/bin/env python3

import sys

dic = {
    '9999': 'Z',
    '999' : 'Y',
    '99'  : 'X',
    '9'   : 'W',
    '888' : 'V',
    '88'  : 'U',
    '8'   : 'T',
    '7777': 'S',
    '777' : 'R',
    '77'  : 'Q',
    '7'   : 'P',
    '666' : 'O',
    '66'  : 'N',
    '6'   : 'M',
    '555' : 'L',
    '55'  : 'K',
    '5'   : 'J',
    '444' : 'I',
    '44'  : 'H',
    '4'   : 'G',
    '333' : 'F',
    '33'  : 'E',
    '3'   : 'D',
    '222' : 'C',
    '22'  : 'B',
    '2'   : 'A'
}

def info():
    print("Usage: t9 <options> MESSAGE")
    print("OPTIONS")
    print("-------")
    print("-d   decrypt message")
    print("-e   encrypt message")


def encrypt(message):
    for element in dic:
        message = message.replace(dic[element], element)
    return message

def decrypt(message):
    for element in dic:
        message = message.replace(element, dic[element])
    return message

def main():
    
    if len(sys.argv) < 2:
        print("[!] ERROR: Not enough arguments")
        return
    mode = True
    
    # argument parsing
    for arg in sys.argv:

        if arg == "-e":
            mode = False

        elif arg == "-d":
            mode = True

        elif arg == "--help" or arg == "-h":
            info()
            break

    message = sys.argv[len(sys.argv) - 1].upper()


    if mode:
        message = decrypt(message)
    else:
        message = encrypt(message)

    print(message)

if __name__ == "__main__":
    main()
