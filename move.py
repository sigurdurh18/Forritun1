LIMIT_RIGHT=10#constant
LIMIT_LEFT=1#constant

def condishon(arg):
    return arg=='r' or arg=='l'

def looped():
    print("l - for moving left\nr - for moving right\nAny other letter for quitting")
    return input("Input your choice: ")

def resault(arg,pos):
    if(arg=='l' and pos>LIMIT_LEFT):
        pos-=1
    elif(arg=='r' and pos<LIMIT_RIGHT):
        pos+=1
    print("New position is:",pos)
    return pos

def looping(k,pos):
    while condishon(k):
        k=looped()
        pos=resault(k,pos)


def innit():
    looping('l',int(input("Input a position between 1 and 10: ")))

innit()