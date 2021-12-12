# Global Variables

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

player_id = "X"
continue_game = True

#Functions
def print_board():
  print(board[0], board[1], board[2])
  print(board[3], board[4], board[5])
  print(board[6], board[7], board[8])

def game():
  print_board()

  while continue_game:

    place_mark(player_id)
    alternate_player()

def alternate_player():
  global player_id
  if player_id == "X":
    player_id = "O"
  elif player_id == "O":
    player_id = "X"


def place_mark(player):

  print(player + "'s turn to pick a spot.")
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

# Starts the game
game()

