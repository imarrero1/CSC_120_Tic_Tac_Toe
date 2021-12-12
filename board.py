# Global Variables
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

player_id = "X"
continue_game = True
winner = None

#Functions
def print_board():
  print(board[0], board[1], board[2])
  print(board[3], board[4], board[5])
  print(board[6], board[7], board[8])

def game():
  print_board()

  while continue_game:

    place_mark(player_id)
    check_continue()
    alternate_player()

  if winner == "X" or winner == "O":
    print(winner, " is the winner!")
  elif winner == None:
    print("There is no winner. Tie game.")

def alternate_player():
  global player_id
  if player_id == "X":
    player_id = "O"
  elif player_id == "O":
    player_id = "X"


def place_mark(player):

  print(player, "'s turn to pick a spot.")
  spot = input("Choose a spot on the board from 1-9: ")

  open = False
  while not open:

    while spot not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      spot = input("Please pick a spot from 1-9: ")
    spot = int(spot) - 1

    if board[spot] == "-":
      open = True
    else:
      print("You can't put a mark in that spot because there is already a mark there. Please try again.")

  board[spot] = player
  print_board()

def check_continue():
  check_win()
  check_tie()


def check_win():
  global winner
  row_win = rows()
  column_win = columns()
  diagonal_win = diagonals()

  if row_win:
    winner = row_win
  elif column_win:
    winner = column_win
  elif diagonal_win:
    winner = diagonal_win
  else:
    winner = None

def diagonals():
  global continue_game
  diagonal_win_1 = board[0] == board[4] == board[8] != "-"
  diagonal_win_2 = board[2] == board[4] == board[6] != "-"

  if diagonal_win_1 or diagonal_win_2:
    continue_game = False

  if diagonal_win_1:
    return board[0]
  elif diagonal_win_2:
    return board[2]

  else:
    return None

def rows():
  global continue_game
  row_win_1 = board[0] == board[1] == board[2] != "-"
  row_win_2 = board[3] == board[4] == board[5] != "-"
  row_win_3 = board[6] == board[7] == board[8] != "-"

  if row_win_1 or row_win_2 or row_win_3:
    continue_game = False

  if row_win_1:
    return board[0]
  elif row_win_2:
    return board[3]
  elif row_win_3:
    return board[6]
  else:
    return None

def columns():
  global continue_game

  column_win_1 = board[0] == board[3] == board[6] != "-"
  column_win_2 = board[1] == board[4] == board[7] != "-"
  column_win_3 = board[2] == board[5] == board[8] != "-"

  if column_win_1 or column_win_2 or column_win_3:
    continue_game = False

  if column_win_1:
    return board[0]
  elif column_win_2:
    return board[1]
  elif column_win_3:
    return board[2]

  else:
    return None

def check_tie():
  global continue_game
  if "-" not in board:
    continue_game = False
    return True
  else:
    return False

# Starts the game
game()








