from turtle import pos
import random


def display(board):
   print(board[7]+'|'+board[8]+'|'+board[9])
   print('-----')
   print(board[4]+'|'+board[5]+'|'+board[6])
   print('-----')
   print(board[1]+'|'+board[2]+'|'+board[3])

def position_choice(board):
    choice = 0
    acceptable_values = [1,2,3,4,5,6,7,8,9]
    
    while choice not in acceptable_values or space_check(board,choice) == False:
        choice = int(input('Pick a position (1-9): '))
        if choice not in acceptable_values:
            print('Sorry, invalid choice')
        if space_check(board,choice) == False:
            print('This field is already taken!')
    return choice

def replacement_choice(board,position,mark):
    board[position] = mark
    return board

def gameon_choice():
    choice = 'WRONG'
    while choice not in ['Y', 'N']:
        choice = input('Do you want to play? (Y/N): ')
        if choice not in ['Y', 'N']:
            print('Sorry, invalid choice')
    if choice == 'Y':
        return True
    else:
        return False
    
def choose_first():
    x = random.randint(1,3)
    if x == 1:
        return True
    elif x == 2:
        return False
    
def player_input():
    mark = ''
    while mark not in ['X','O']:
        mark = input("Please pick a marker X or O: ")
        if mark not in ['X','O']:
            print('Sorry, invalid choice')
    if mark == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


def space_check(board,position):
    if board[position] == ' ':
        return True
    else:
        return False
    
def win(board,mark):
    if(board[1] == mark and board[2] == mark and board[3] == mark):
        return True
    elif(board[4] == mark and board[5] == mark and board[6] == mark):
        return True
    elif(board[7] == mark and board[8] == mark and board[9] == mark):
        return True
    elif(board[1] == mark and board[5] == mark and board[9] == mark):
        return True
    elif(board[7] == mark and board[5] == mark and board[3] == mark):
        return True
    elif(board[1] == mark and board[4] == mark and board[7] == mark):
        return True
    elif(board[2] == mark and board[5] == mark and board[8] == mark):
        return True
    elif(board[3] == mark and board[6] == mark and board[9] == mark):
        return True
    else:
        return False

def full_board_check(board):   
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True
        
def replay():
    choice = 'WRONG'
    while choice not in ['Y', 'N']:
        choice = input('Do you want to play again? (Y/N): ')
        if choice not in ['Y', 'N']:
            print('Sorry, invalid choice')
    if choice == 'Y':
        return True
    else:
        return False
    



print('Welcome to Tic Tac Toe!')

while True:
    game_on = True
    board = [' '] * 10
    player_1,player_2 = player_input()
    turn = choose_first()
    if turn == True:
        print('Player 1 goes first!')
    else:
        print('Player 2 goes first!')

    game_on = gameon_choice()
    
    while game_on:
        position = position_choice(board)
        if turn:
            replacement_choice(board,position,player_1)
            turn = False
            if win(board,player_1):
                display(board)
                print(f'{player_1} won!')
                break
            if full_board_check(board):
                display(board)
                print('The game is a draw!')
                break
            display(board)
        else:
            replacement_choice(board,position,player_2)
            turn = True
            if win(board,player_2):
                display(board)
                print(f'{player_2} won!')
                break
            if full_board_check(board):
                display(board)
                print('The game is a draw!')
                break
            display(board)
    if not replay():
        break