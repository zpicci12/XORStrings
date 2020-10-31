import sys

def solve(mode, key_word, inp):
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
        if (mode == "human"):
            str += chr(ord(inp[i]) ^ ord(key[i]))
        else:
            str += (hex(ord(inp[i]) ^ ord(key[i])))[2:] + " "
    print(str)

'''
def solve_hex(key_word, inp):
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
        str += (hex(ord(inp[i]) ^ ord(key[i])))[2:] + " "
    print(str)
'''

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

    #note to self: incorporate mode into argument once finished w part 2
    if (mode == "numOut" or mode == "human"):
        solve(mode, key, inp)
    else:
        print("Not a valid mode. Please select 'human' or 'numOut.'")

    #solve_hex(mode, key, inp)
