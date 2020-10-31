'''
Zoe Piccirillo
Cybersecurity Period 5
November 2, 2020

XORStrings: encode/decode messages using the XOR operator.

Usage: "make run ARGS="mode keyfile textfile"
'''

import sys

def solve(mode, key_word, inp): #perform XOR operation on key and input text
    key = key_word
    count = 0
    while (len(key) < len(inp)): #loop key until it is the length of the input text
        key = key + key_word[count]
        if (count == len(key_word) - 1):
            count = 0
        else:
            count += 1
    str = ""
    for i in range(len(inp)): #XOR each character of input text and key; convert to ASCII (human mode) or hex value (numOut)
        if (mode == "human"):
            str += chr(ord(inp[i]) ^ ord(key[i]))
        else:
            str += (hex(ord(inp[i]) ^ ord(key[i])))[2:] + " " #remove ("0x") from beginning of hex value
    print(str)

if __name__ == "__main__":
    mode = sys.argv[1]
    keyfile = sys.argv[2]
    inpfile = sys.argv[3]
    key = open(keyfile).read()[:-1] #removes the mandatory \n at the end of the file to support one line messages.
    inp = open(inpfile).read()[:-1] #removes the mandatory \n at the end of the file to support one line messages.
    debug = False

    if(debug):
        print("mode:"+mode)
        print("key: "+key)
        print("inp: "+inp)

    if (mode == "numOut" or mode == "human"):
        solve(mode, key, inp)
    else: #mode is not "numOut" or "human"
        print("Not a valid mode. Please select 'human' or 'numOut.'")
