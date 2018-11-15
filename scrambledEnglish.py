import random
import string
'''
Data structure:
[
line [word[c,c,c],word[c,c,c]]
line [word[c,c,c],word[c,c,c]]
line [word[c,c,c],word[c,c,c]]
line [word[c,c,c],word[c,c,c]]
]
'''

def get_word_string(filename):
    try:
        with open(filename) as fil:
            return [[[c for c in word ] for word in line.strip('\n').split(' ')] for line in fil]
    except Exception as e:
        print("File",filename,"not found")

def scramble(li):#takes in list and returns a scrabled list
    if li[-1] not in string.punctuation:
        num=0
    else:
        num=1
    if len(li)>3+num:
        x = li[1:-1-num]
        random.shuffle(x)
        return [li[0]] + x + li[-1-num:]
    else:
        return li

def massToString(li):
    stringed=""
    for line in li:
        for word in line:
            stringed+=''.join(word)+' '
    return stringed

def scramble_string(txt):
    for line in range(len(txt)):
        for word in range(len(txt[line])):
            txt[line][word]=scramble(txt[line][word])
    txt[-1][-1]=scramble(txt[-1][-1])
    return massToString(txt)
     

# Main program starts here - DO NOT change it
random.seed(10)
filename = "test.txt"#input("Enter name of file: ")
word_string = get_word_string(filename)
scrambled_string = scramble_string(word_string)
print(scrambled_string)

print([] is None)
print(None in [])
try:
    pass
except