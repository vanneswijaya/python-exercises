import random

board = [' ' for x in range(10)]

def main():
    print ('TIC TAC TOE') 
    print ('===========')
    print ('Complete a straight line to win the game')
    print ('(Diagonal/Horizontal/Vertical')
    print ('The board has positions 1-9 starting at the top left')
    user1 = input('Enter player one name : ')
    user2 = input('Enter player two name : ')
    while True:
        printBoard()
        pos1 = enterPos('X')
        insertLetter('X', pos1)
        print(f'{user1} placed an "X" in position {pos1}:')
        win1 = winner(board, 'X')
        win2 = winner(board, 'O')
        conclusion(win1, win2, user1, user2)
        printBoard()
        pos2 = enterPos('O')
        insertLetter('O', pos2)
        print(f'{user2} placed an "O" in position {pos2}:')
        win1 = winner(board, 'X')
        win2 = winner(board, 'O')
        conclusion(win1, win2, user1, user2)
        
def printBoard():
    print ('------------------')
    print ('  {}  |  {}  |  {}'.format(board[1], board[2], board[3]))
    print ('------------------')
    print ('  {}  |  {}  |  {}'.format(board[4], board[5], board[6]))
    print ('------------------')
    print ('  {}  |  {}  |  {}'.format(board[7], board[8], board[9]))
    print ('------------------')

def enterPos(le):
    ask = int(input(f'Select a position to place "{le}" (1-9): '))
    return ask

def insertLetter(letter, pos):
    board[pos] = letter

def winner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or 
    (bo[4] == le and bo[5] == le and bo[6] == le) or
    (bo[1] == le and bo[2] == le and bo[3] == le) or 
    (bo[7] == le and bo[4] == le and bo[1] == le) or 
    (bo[8] == le and bo[5] == le and bo[2] == le) or 
    (bo[9] == le and bo[6] == le and bo[3] == le) or 
    (bo[7] == le and bo[5] == le and bo[3] == le) or 
    (bo[9] == le and bo[5] == le and bo[1] == le)) 

def conclusion(win1, win2, user1, user2):
    if win1:
        printBoard()
        print (f'{user1} won!')
        quit()
    elif win2:
        printBoard()
        print (f'{user2} won!')
        quit()
    elif board.count(' ') == 1:
        printBoard()
        print ('It is a tie!')
        quit()
    else:
        pass

main()
