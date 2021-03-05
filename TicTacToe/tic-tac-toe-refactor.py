# Tic Tac Toe
# Reference: With modification from http://inventwithpython.com/chapter10.html. 
import random

SPACES = 10

def draw_board(board):
    """
    Prints out the board that it was passed,'board' is a list 
        of 10 strings representing the board(ignore index 0).
    """
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def input_player_letter():
    """
    Lets player type which letter they want to be and returns
    a list with player’s letter as first item in the list and 
    computer's letter as the second.
    """ 
    letter = ''
    while not (letter == 'X' or letter == 'O'):
      print("Do you want to be X or O?")
      letter = input().upper()

    if letter == 'X':
      return ['X', 'O']                  
    return ['O', 'X']

def who_goes_first():
    """
    Randomly chooses the player who will go first.
    """
    if random.randint(0, 1) == 0:
      return 'computer'                  
    return 'player'

def play_again():
    """"
    Returns True if the player wants to play again, 
    otherwise it returns False.
    """
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def make_move(board, letter, move):
    board[move] = letter

def is_winner(bo, le):
    """
    Given a board and a player’s letter, it returns True if player has won.
    Uses bo for board and le for letter.
    """
    top = (bo[7] == le and bo[8] == le and bo[9] == le)
    mid = (bo[4] == le and bo[5] == le and bo[6] == le)
    bottom = (bo[1] == le and bo[2] == le and bo[3] == le)
    down_left = (bo[7] == le and bo[4] == le and bo[1] == le)
    down_mid = (bo[8] == le and bo[5] == le and bo[2] == le)
    down_right = (bo[9] == le and bo[6] == le and bo[3] == le)
    diagonal = (bo[7] == le and bo[5] == le and bo[3] == le)
    an_diagonal = (bo[1] == le and bo[5] == le and bo[9] == le)

    return top or mid or bottom or down_left or down_right or \
           down_mid or diagonal or an_diagonal

def get_board_copy(board):
    """
    Makes a duplicate of the board list and returns it.
    """
    dupe_board = []
    for i in range(0, len(board)):
        dupe_board.append(board[i])
    return dupe_board

def is_space_free(board, move):
    """
    Returns true if passed move is free on passed board.
    """
    if board[move] == ' ':
      return True

def get_player_move(board):
    """
    Player inputs in their move.
    """
    player_move = ' ' 
    while player_move not in '1 2 3 4 5 6 7 8 9'.split() \
            or  not is_space_free(board, int(player_move)):
        print('What is your next move? (1-9)')
        player_move = input()
    return int(player_move)

def choose_random_move_from_list(board, moves_list):
    """
    Returns valid move from the passed list on passed board or 
    None if there is no valid move.
    """
    possible_moves = []
    for i in moves_list:
      if is_space_free(board, i):
        possible_moves.append(i)

    if len(possible_moves) != 0: 
        return random.choice(possible_moves)
    return None

def get_computer_move(board, computer_letter): #https://stackoverflow.com/a/25000042/81306
    """
    Given a board and computer's letter it determines where 
    to move and returns that move.
    """
    if computer_letter == 'X':
      player_letter = 'O'
    else:
      player_letter = 'X'

    # Here is our algorithm for our Tic Tac Toe AI:
    # First, check if we can win in the next move
    for i in range(1, SPACES):
      copy = get_board_copy(board)
      if is_space_free(copy, i):
        make_move(copy, computer_letter, i)
        if is_winner(copy, computer_letter):
            return i

    # Check if the player could win on their next move, and block them.
    for i in range(1, SPACES):
      copy = get_board_copy(board)
      if is_space_free(copy, i):
        make_move(copy, player_letter, i)
        if is_winner(copy, player_letter):
          return i

    # Try to take one of the corners, if they are free.
    move = choose_random_move_from_list(board, [1, 3, 7, 9])
    if move:
      return move

    # Try to take the center, if it is free.
    if is_space_free(board, 5):
      return 5

    # Move on one of the sides.
    return choose_random_move_from_list(board, [2, 4, 6, 8])

def is_board_full(board):
    """
    Returns True if every space on the board has been taken, 
    otherwise returns False.
    """
    for i in range(1, SPACES):
      if is_space_free(board, i):
        return False
    return True

def reset_board():
  """ 
    Resets the board. 
  """
  board = [' '] * SPACES 
  player_letter, computer_letter = input_player_letter()
  turn = who_goes_first()
  print('The ' + turn + ' will go first.')
  return player_letter, computer_letter, turn, board

def players_turn(player_letter, board):
  """
  Player's turn to make a move.
  """
  # draw_board(board)
  move = get_player_move(board)
  make_move(board, player_letter, move)

def computers_turn(computer_letter, board):
  """
  Computer's turn to make a move.
  """
  move = get_computer_move(board, computer_letter)
  make_move(board, computer_letter, move)

def game_is_playing(board, computer_letter, turn, player_letter):
  """
    If someone wins, it prints a congrats message else it switches players turn to input move
    or if there are no more turns left then it sets the game as a tie. 
  """
  while True:
    if turn == 'player':
      players_turn(player_letter, board)
      if is_winner(board, player_letter):
        draw_board(board)
        print('Hooray! You have won the game!')
        break
      if is_board_full(board):
        draw_board(board)
        print('The game is a tie!')
        break
      turn = 'computer'
    else: 
      computers_turn(computer_letter, board)
      if is_winner(board, computer_letter):
        draw_board(board)
        print('The computer has beaten you! You lose.')
        break
      if is_board_full(board):
        draw_board(board)
        print('The game is a tie!')
        break
      turn = 'player'

if __name__ == "__main__":
  print('Welcome to Tic Tac Toe!')
  while True:
    player_letter, computer_letter, turn, board = reset_board()
    game_is_playing(board, computer_letter, turn, player_letter)
    if not play_again():
      break