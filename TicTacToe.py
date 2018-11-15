PLAYERS={False:'X',True:'O'}

def creation(length):#finished but no error handeling
    return [[1+q+i*length for q in range(length)] for i in range(length)]

def display(kek):#finished
    for i in kek:
        for q in i:
            print('{:>5}'.format(q),end="")
        print()

def innit():#finished up to error message
    while True:
        try:
            kek = int(input("Input dimension of the board: "))
            if kek>2:
                return creation(kek)
            else:
                throw
        except Exception as e:
            print("")

def victoryCheck(gameBoard,pl):
    posible=[]
    sideCheck=0
    goal=len(gameBoard)
    for i in range(goal):
        if gameBoard[i][i]==PLAYERS[pl]:
            posible.append(i)
        if gameBoard[i][-1-i]==PLAYERS[pl]:
            sideCheck+=1
    if len(posible) == goal or sideCheck==goal:
        return True
    for i in posible:
        lod=1
        lad=1
        for q in [z for z in range(goal) if z !=i]:
            if gameBoard[i][q]==PLAYERS[pl]:
                lad+=1
            if gameBoard[q][i]==PLAYERS[pl]:
                lod+=1
        if lod==goal or lad==goal:
            return True
    return False

def action(gameBoard,pl):
    length=len(gameBoard)#might need to recall this value more then once
    while True:
        try:
            inp = int(input("{} position: ".format(PLAYERS[pl])))-1#throws error if input is not an int. also shifts the input to fit list index standard
            if(gameBoard[int(inp//length)][int(inp%length)] not in PLAYERS.values()):#throws an error if it's out of bounce
                gameBoard[int(inp//length)][int(inp%length)]=PLAYERS[pl]#throws an error if it's out of bounce
                return
            else:
                print('Illegal move!')
        except Exception as e:
            print('Illegal move!')


def gameLoop(gameBoard):
    pl=True
    while(not victoryCheck(gameBoard,pl)):
        pl= not pl
        display(gameBoard)
        action(gameBoard,pl)
    display(gameBoard)
    return pl

def main():
    gameBoard=innit()
    victor=gameLoop(gameBoard)
    print("Winner is:",PLAYERS[victor])

main()