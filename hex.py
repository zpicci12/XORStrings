'''
import sys
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
'''


def solve(key_word, inp):
    key = key_word
    count = 0
    while (len(key) < len(inp)):
        key = key + key_word[count]
        if (count == len(key_word) - 1):
            count = 0
        else:
            count += 1
    str = ""
    for i in range(len(inp)):
        str += chr(ord(inp[i]) ^ ord(key[i]))
    print(inp)
    print(str)

solve("A", "hello")
solve("FISH", " this is a test")
