
import random
board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
available = [str(num) for num in range(0,10)] # a List Comprehension
Players = {'X':'','O':''}
def player_input(rand_int_player):
    chosen_marker = ''
    left_marker = ''
    while chosen_marker.upper() not in ('X','O'):
        chosen_marker = input("Do you wanna be X or O: ")
        if chosen_marker.upper() not in ('X','O'):
            print("Please choose again")
    print("Your marker is {}".format(chosen_marker))
    if chosen_marker.upper() == 'X':
    	left_marker = 'O'
    else:
    	left_marker = 'X'
    if rand_int_player == 1:
    	Players[chosen_marker.upper()] = 'Player1'
    	Players[left_marker] = 'Player2'
    	#print(Players[chosen_marker.upper()] +' ' + chosen_marker + " TEST")
    	#print(Players[left_marker] + ' ' +left_marker + " TEST")
    else:
    	Players[chosen_marker.upper()] = 'Player2'
    	Players[left_marker] = 'Player1'
    	#print(Players[chosen_marker.upper()] + ' ' +chosen_marker + " TEST")
    	#print(Players[left_marker] + ' ' +left_marker + " TEST")
    	
    game_start(chosen_marker.upper())
    replay()

def player_to_start():
    player1 = random.randint(0,1)
    if player1 == 1:
        print("Player 1 goes first")
        player_input(player1)
    else:
        print("Player 2 goes first")
        player_input(player1)

def ready():
    entered_answer = input("Are you ready?")
    if(entered_answer.lower() =='yes'):
        player_to_start()
    else:
        print("Ok see you next time")


def display_board(a,b):
	#index = 0
   	print('Available   TIC-TAC-TOE\n'+
           '  moves\n\n  '+
          a[7]+'|'+a[8]+'|'+a[9]+'        '+b[7]+'|'+b[8]+'|'+b[9]+'\n  '+
          '-----        -----\n  '+
          a[4]+'|'+a[5]+'|'+a[6]+'        '+b[4]+'|'+b[5]+'|'+b[6]+'\n  '+
          '-----        -----\n  '+
          a[1]+'|'+a[2]+'|'+a[3]+'        '+b[1]+'|'+b[2]+'|'+b[3]+'\n')

def win_check(board, mark):
    if (board[1] + board[2] + board[3] == 3*mark):
        return True,mark
    elif (board[4] + board[5] + board[6] == 3*mark):
        return True,mark
    elif (board[7] + board[8] + board[9] == 3*mark):
        return True,mark
    elif (board[1] + board[4] + board[7] == 3*mark):
        return True,mark
    elif (board[2] + board[5] + board[8] == 3*mark):
        return True,mark
    elif (board[3] + board[6] + board[9] == 3*mark):
        return True,mark
    elif (board[1] + board[5] + board[9] == 3*mark):
        return True,mark
    elif (board[3] + board[5] + board[7] == 3*mark):
        return True,mark
    else:
        return False,mark


def is_full(board):
    isfull = True
    for i in range(1,10):
        if board[i] == ' ':
            isfull = False
    return isfull


def marker_placer(board,marker):
    right_position = False
    while right_position == False:
        player_position = int(input("Choose your position: "))
        if board[player_position] == ' ':
            break
        print('Position is not available')
    board[player_position] = marker
    #display_board(board)



def game_start(chosen_marker):
    marker = chosen_marker
    isfull = False
    iswinner = False
    while isfull is False:
        marker_placer(board,marker)
        print('\n'*10)
        display_board(available,board)
        isfull = is_full(board)
        iswinner = win_check(board,marker)[0]
        if iswinner is True:
        	winner_mark = win_check(board,marker)[1]
        	print(Players[winner_mark] +" Has won") 
        	break
        if iswinner is False and isfull is True:
        	print("Draw")
        if marker == 'X':
            marker = 'O'
        else:
            marker = 'X'
def replay():
	reply = input("Wanna play again? ")
	if reply == 'yes':
		global board# = 
		board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
		ready()
	else:
		print("See you next time")
       
    

ready()
