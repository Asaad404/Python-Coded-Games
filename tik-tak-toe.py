import os,time
def displayGrid():
    global grid
    print(str(grid[0][0])+" | "+str(grid[0][1])+" | "+str(grid[0][2]))
    print("-"*10)
    print(str(grid[1][0])+" | "+str(grid[1][1])+" | "+str(grid[1][2]))
    print("-"*10)
    print(str(grid[2][0])+" | "+str(grid[2][1])+" | "+str(grid[2][2]))
def fillSlot(s,XO):
    global grid
    if (s < 1 or s > 9):
        return False
    if (s == 1):
        if (grid[0][0]!= 1):
            return False
        grid[0][0] = XO
    if (s == 2):
        if (grid[0][1] != 2):
            return False
        grid[0][1] = XO
    if (s == 3):
        if (grid[0][2] != 3):
            return False
        grid[0][2] = XO
    if (s == 4):
        if (grid[1][0] != 4):
            return False
        grid[1][0] = XO
    if (s == 5):
        if (grid[1][1] != 5):
            return False
        grid[1][1] = XO
    if (s ==6):
        if(grid[1][2]!=6):
            return False
        grid[1][2] = XO
    if (s == 7):
        if (grid[2][0] != 7):
            return False
        grid[2][0] = XO
    if (s == 8):
        if (grid[2][1] != 8):
            return False
        grid[2][1] = XO
    if (s == 9):
        if (grid[2][2] != 9):
            return False
        grid[2][2] = XO
    return True
def isWinner():
    if ((grid[0][0]==grid[0][1]==grid[0][2]) or (grid[1][0]==grid[1][1]==grid[1][2]) or (grid[2][0]==grid[2][1]==grid[2][2]) or (grid[0][0]==grid[1][0]==grid[2][0]) or (grid[0][1]==grid[1][1]==grid[2][1]) or (grid[0][2]==grid[1][2]==grid[2][2]) or (grid[0][0]==grid[1][1]==grid[2][2]) or (grid[0][2]==grid[1][1]==grid[2][0])):
        return True
    else:
        return False
#Main Program
grid=[[1,2,3],[4,5,6],[7,8,9]]
turns=1
displayGrid()
while turns<10:
    n=(-1)**turns
    if n==-1:
        b=False
        while b==False:
            print('Player 1 turn')
            a = eval(input('Choose a slot: '))
            b=fillSlot(a,'X')
            if b==False:
                print('Choose valid slot')
        os.system('cls')
        displayGrid()
        turns+=1
        if isWinner():
            print('Player 1 wins')
            time.sleep(1)
            break
        else:
            if turns==10:
                print('Its a Draw')
                time.sleep(1)
                break
    if n==1:
        b = False
        while b==False:
            print('Player 2 turn')
            a = eval(input('Choose a slot: '))
            b=fillSlot(a,'O')
            if b==False:
                print('Choose valid slot')
        os.system('cls')
        displayGrid()
        turns+=1
        if isWinner():
            print('Player 2 wins')
            time.sleep(1)
            break
        else:
            if turns==10:
                print('Its a Draw')
                time.sleep(1)
                break