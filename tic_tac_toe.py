# Note that input() takes in a string. If you need an integer value, use

def display_board(board):
    print('\n'*100)
    print(board[7]+' | '+board[8]+' | '+board[9])
    print('---'+'---'+'---')
    print(board[4]+' | '+board[5]+' | '+board[6])
    print('---'+'---'+'---')
    print(board[1]+' | '+board[2]+' | '+board[3])

def player_input():
    marker = ' '
    while not (marker=='X' or marker=='O') :
        marker=input('Player 1: Do you want to be X or O? ').upper()
    if marker=='X':
        return ('X','O')
    else:
        return ('O','X')
    
# Step 3: Write a function that takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board.

def place_marker(board, marker, position):
    board[position]=marker
    
# Step 4: Write a function that takes in a board and a mark (X or O) and then checks to see if that mark has won.


def win_check(board, mark):

    return  (board[1]==mark and board[2]==mark and  board[3]==mark) or (board[4]==mark and board[5]==mark and  board[6]==mark) or (board[7]==mark and board[8]==mark and  board[9]==mark) or (board[1]==mark and board[4]==mark and  board[7]==mark) or (board[2]==mark and board[5]==mark and  board[8]==mark) or (board[3]==mark and board[6]==mark and  board[9]==mark) or (board[7]==mark and board[5]==mark and  board[3]==mark) or (board[1]==mark and board[5]==mark and  board[9]==mark)
    
    

# TEST Step 4: run the win_check function against our test_board - it should return True

# Step 5: Write a function that uses the random module to randomly decide which player goes first. You may want to lookup random.randint() Return a string of which player went first.

import random
def choose_first():
    if random.randint(0,1)==0:
        return 'player1'
    else:
        return 'Player2'

# Step 6: Write a function that returns a boolean indicating whether a space on the board is freely available.

def space_check(board, position):
    return board[position] == ' '

# Step 7: Write a function that checks if the board is full and returns a boolean value. True if full, False otherwise.


def full_board_check(board):
    for i in range (1,10):
        if space_check(board,i):
            return False
    return True
    

# Step 8: Write a function that asks for a player's next position (as a number 1-9) and then uses the function from step 6 to check if it's a free position. If it is, then return the position for later use.

def player_choice(board):
    position=0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position=int(input("Enter your next position between 1 to 9 :"))
        #position = int(input('Please enter a number'))
    return position


# Step 9: Write a function that asks the player if they want to play again and returns a boolean True if they do want to play again.


def replay():
    return input("Do you want to play again ?, Enter Yes or No ").lower().startswith('y')
    
# Step 10: Here comes the hard part! Use while loops and the functions you've made to run the game!


print('Welcome to Tic Tac Toe!')

while True:
    myboard = [' ']*10
    player1_marker,player2_marker=player_input()
    turn=choose_first()
    print(turn+" Will go First")
    play_game=input('Are you ready to play? Enter Yes or No.')
    # Set the game up here
    if play_game.lower()[0]=='y':
        game_on= True
    else:
        game_on=False


    while game_on:
        #Player 1 Turn
        if turn =='player1':

            display_board(myboard)
            position=player_choice(myboard)
            place_marker(myboard,player1_marker,position)

            if win_check(myboard,player1_marker):
                display_board(myboard)
                print("Player 1 won")
                game_on=False
            else:
                if full_board_check(myboard):
                    display_board(myboard)
                    print("This Game ia a Draw")
                    break
                else:
                    turn = 'player2'
        else:

            # Player2's turn.        
            display_board(myboard)
            position=player_choice(myboard)
            place_marker(myboard,player2_marker,position)
            if win_check(myboard,player2_marker):
                display_board(myboard)
                print("Player 2 won")
                game_on=False
            else:
                if full_board_check(myboard):
                    display_board(myboard)
                    print("This Game ia a Draw")
                    break
                else:
                    turn = 'player1'

    if not replay():
        break