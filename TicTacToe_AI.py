# --- Some variables ---
import random, os, sys
from sys import platform

easy = ["e", "easy", "E", "Easy"]
medium = ["m", "medium", "M", "Medium"]
hard = ["h", "hard", "H", "Hard"]
impossible = ["i", "impossible", "I", "Impossible"]
newGameAnswers = ["y", "yes", "Yes", "YES",  "Y"]
board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
player = "X"
winner = None
gameRunning = True

# define clear function
if platform == "linux" or platform == "linux2" or platform == "darwin":
  clear = lambda: os.system('clear')
elif platform == "win32":
  clear = lambda: os.system('cls')
else:
  print("Unknown platform", file = sys.stderr)

# --- Print the game board ---
def printGameBoard(board):
  print("\n" + board[0] + " | " + board[1] + " | " + board[2])
  print("---------")
  print(board[3] + " | " + board[4] + " | " + board[5])
  print("---------")
  print(board[6] + " | " + board[7] + " | " + board[8])

# --- Take player input ---
def playerInput(board):
  inp = input("\nPlease, enter a number between 1 and 9: ")
  clear()
  if inp.strip().isdigit():
    inp = int(inp)
    if inp >= 1 and inp <= 9 and board[inp-1] == "-":
      board[inp-1] = player
    elif inp < 1 or inp > 9:
      print("\nIt looks like you entered a wrong number...")
      playerInput(board)
    else:
      print("\nOps...player is already in that spot!")
      playerInput(board)
  else:
    print("\nIt looks like you haven't entered a number...")
    playerInput(board)
    
# --- Check for horizontal winner ---
def checkHorizontal(board):
  global winner
  if board[0] == board[1] == board[2] and board[0] != "-":
    winner = board[0]
    return True
  elif board[3] == board[4] == board[5] and board[3] != "-":
    winner = board[3]
    return True
  elif board[6] == board[7] == board[8] and board[6] != "-":
    winner = board[6]
    return True

# --- Check for vertical winner ---
def checkVertical(board):
  global winner
  if board[0] == board[3] == board[6] and board[0] != "-":
    winner = board[0]
    return True
  elif board[1] == board[4] == board[7] and board[1] != "-":
    winner = board[1]
    return True
  elif board[2] == board[5] == board[8] and board[2] != "-":
    winner = board[2]
    return True

# --- Check for diagonal winner ---
def checkDiagonal(board):
  global winner
  if board[0] == board[4] == board[8] and board[0] != "-":
    winner = board[0]
    return True
  elif board[2] == board[4] == board[6] and board[2] != "-":
    winner = board[2]
    return True

# --- Check for tie ---
def checkTie(board):
  global gameRunning
  if "-" not in board:
    print("\nTie!")
    printGameBoard(board)
    gameRunning = False
    return True
  return False

# --- Check for winner ---
def checkWinner():
  global gameRunning
  if checkHorizontal(board) or checkVertical(board) or checkDiagonal(board):
    print(f"\nThe winner is {winner}")
    printGameBoard(board)
    gameRunning = False
    return True
  return False

# --- Medium difficulty ---
def checkPlayerMedium(board):
  if "X" in board[0] and "X" in board[1] and board[2] == "-":
    return 2
  if "X" in board[1] and "X" in board[2] and board[0] == "-":
    return 0
  if "X" in board[0] and "X" in board[2] and board[1] == "-":
    return 1
  if "X" in board[3] and "X" in board[4] and board[5] == "-":
    return 5
  if "X" in board[3] and "X" in board[5] and board[4] == "-":
    return 4
  if "X" in board[4] and "X" in board[5] and board[3] == "-":
    return 3
  if "X" in board[6] and "X" in board[7] and board[8] == "-":
    return 8
  if "X" in board[6] and "X" in board[8] and board[7] == "-":
    return 7
  if "X" in board[7] and "X" in board[8] and board[6] == "-":
    return 6
  if "X" in board[0] and "X" in board[3] and board[6] == "-":
    return 6
  if "X" in board[0] and "X" in board[6] and board[3] == "-":
    return 3
  if "X" in board[3] and "X" in board[6] and board[0] == "-":
    return 0
  if "X" in board[1] and "X" in board[4] and board[7] == "-":
    return 7
  if "X" in board[1] and "X" in board[7] and board[4] == "-":
    return 4
  if "X" in board[4] and "X" in board[7] and board[1] == "-":
    return 1
  if "X" in board[2] and "X" in board[5] and board[8] == "-":
    return 8
  if "X" in board[2] and "X" in board[8] and board[5] == "-":
    return 5
  if "X" in board[5] and "X" in board[8] and board[2] == "-":
    return 2
  if "X" in board[0] and "X" in board[4] and board[8] == "-":
    return 8
  if "X" in board[0] and "X" in board[8] and board[4] == "-":
    return 4
  if "X" in board[4] and "X" in board[8] and board[0] == "-":
    return 0
  if "X" in board[2] and "X" in board[4] and board[6] == "-":
    return 6
  if "X" in board[2] and "X" in board[6] and board[4] == "-":
    return 4
  if "X" in board[4] and "X" in board[6] and board[2] == "-":
    return 2
  else:
    return random.randint(0, 8)

# --- AI for hard level ---
def checkPlayerHard(board):
  if "X" in board[0] and "X" in board[1] and board[2] == "-":
    return 2
  if "X" in board[1] and "X" in board[2] and board[0] == "-":
    return 0
  if "X" in board[0] and "X" in board[2] and board[1] == "-":
    return 1
  if "X" in board[3] and "X" in board[4] and board[5] == "-":
    return 5
  if "X" in board[3] and "X" in board[5] and board[4] == "-":
    return 4
  if "X" in board[4] and "X" in board[5] and board[3] == "-":
    return 3
  if "X" in board[6] and "X" in board[7] and board[8] == "-":
    return 8
  if "X" in board[6] and "X" in board[8] and board[7] == "-":
    return 7
  if "X" in board[7] and "X" in board[8] and board[6] == "-":
    return 6
  if "X" in board[0] and "X" in board[3] and board[6] == "-":
    return 6
  if "X" in board[0] and "X" in board[6] and board[3] == "-":
    return 3
  if "X" in board[3] and "X" in board[6] and board[0] == "-":
    return 0
  if "X" in board[1] and "X" in board[4] and board[7] == "-":
    return 7
  if "X" in board[1] and "X" in board[7] and board[4] == "-":
    return 4
  if "X" in board[4] and "X" in board[7] and board[1] == "-":
    return 1
  if "X" in board[2] and "X" in board[5] and board[8] == "-":
    return 8
  if "X" in board[2] and "X" in board[8] and board[5] == "-":
    return 5
  if "X" in board[5] and "X" in board[8] and board[2] == "-":
    return 2
  if "X" in board[0] and "X" in board[4] and board[8] == "-":
    return 8
  if "X" in board[0] and "X" in board[8] and board[4] == "-":
    return 4
  if "X" in board[4] and "X" in board[8] and board[0] == "-":
    return 0
  if "X" in board[2] and "X" in board[4] and board[6] == "-":
    return 6
  if "X" in board[2] and "X" in board[6] and board[4] == "-":
    return 4
  if "X" in board[4] and "X" in board[6] and board[2] == "-":
    return 2
  if board[4] == "-":
    return 4
  if board[0] == "-":
    return 0
  if board[2] == "-":
    return 2
  if board[6] == "-":
    return 6
  if board[8] == "-":
    return 8
  if player == board[4] and board[0] == "-":
    return 0
  if player == board[4] and board[2] == "-":
    return 2
  if player == board[4] and board[6] == "-":
    return 6
  if player == board[4] and board[8] == "-":
    return 8
  else:
    return random.randint(0, 8)
  
# --- AI for impossible level ---
def checkPlayerImpossible(board):
  if "X" in board[0] and "X" in board[1] and board[2] == "-":
    return 2
  if "X" in board[1] and "X" in board[2] and board[0] == "-":
    return 0
  if "X" in board[0] and "X" in board[2] and board[1] == "-":
    return 1
  if "X" in board[3] and "X" in board[4] and board[5] == "-":
    return 5
  if "X" in board[3] and "X" in board[5] and board[4] == "-":
    return 4
  if "X" in board[4] and "X" in board[5] and board[3] == "-":
    return 3
  if "X" in board[6] and "X" in board[7] and board[8] == "-":
    return 8
  if "X" in board[6] and "X" in board[8] and board[7] == "-":
    return 7
  if "X" in board[7] and "X" in board[8] and board[6] == "-":
    return 6
  if "X" in board[0] and "X" in board[3] and board[6] == "-":
    return 6
  if "X" in board[0] and "X" in board[6] and board[3] == "-":
    return 3
  if "X" in board[3] and "X" in board[6] and board[0] == "-":
    return 0
  if "X" in board[1] and "X" in board[4] and board[7] == "-":
    return 7
  if "X" in board[1] and "X" in board[7] and board[4] == "-":
    return 4
  if "X" in board[4] and "X" in board[7] and board[1] == "-":
    return 1
  if "X" in board[2] and "X" in board[5] and board[8] == "-":
    return 8
  if "X" in board[2] and "X" in board[8] and board[5] == "-":
    return 5
  if "X" in board[5] and "X" in board[8] and board[2] == "-":
    return 2
  if "X" in board[0] and "X" in board[4] and board[8] == "-":
    return 8
  if "X" in board[0] and "X" in board[8] and board[4] == "-":
    return 4
  if "X" in board[4] and "X" in board[8] and board[0] == "-":
    return 0
  if "X" in board[2] and "X" in board[4] and board[6] == "-":
    return 6
  if "X" in board[2] and "X" in board[6] and board[4] == "-":
    return 4
  if "X" in board[4] and "X" in board[6] and board[2] == "-":
    return 2
  if ("X" in board[0] and "X" in board[8] and player in board[4]) or ("X" in board[3] and "X" in board[6] and player in board[4]):
    return random.choice([1,3,5,7])
  if board[4] == "-":
    return 4
  if board[0] == "-":
    return 0
  if board[2] == "-":
    return 2
  if board[6] == "-":
    return 6
  if board[8] == "-":
    return 8
  if player == board[4] and board[0] == "-":
    return 0
  if player == board[4] and board[2] == "-":
    return 2
  if player == board[4] and board[6] == "-":
    return 6
  if player == board[4] and board[8] == "-":
    return 8
  else:
    return random.randint(0, 8)

# --- Switch the player ---
def switchPlayer():
  global player
  if player == "X":
    player = "O"
  else:
    player = "X"

# --- Computer level easy ---
def computerEasy(board):
  while player == "O" and "-" in board:
    pos = random.randint(0,8)
    if board[pos] == "-":
      board[pos] = "O"
      switchPlayer()

# --- Computer level medium ---
def computerMedium(board):
  while player == "O" and "-" in board:
    pos = checkPlayerMedium(board)
    if board[pos] == "-":
      board[pos] = "O"
      switchPlayer()

# --- Computer level hard ---
def computerHard(board):
  while player == "O" and "-" in board:
    pos = checkPlayerHard(board)   
    if board[pos] == "-":
      board[pos] = "O"
      switchPlayer()

# --- Computer level hard ---
def computerImpossible(board):
  while player == "O" and "-" in board:
    pos = checkPlayerImpossible(board)   
    if board[pos] == "-":
      board[pos] = "O"
      switchPlayer()

# --- Clear the board for a new game ---
def resetBoard(board):
  global gameRunning
  for i in range(len(board)):
    board[i] = "-"
  gameRunning = True
  clear()

# --- Easy Game Running ---
def easyGame():
  while gameRunning:
    printGameBoard(board)

    playerInput(board)
    if checkWinner():
      newgame = input("\nNew Game? Press Enter: ")
      if len(newgame) == 0:
        resetBoard(board)
      else:
        print("\nSee you soon!")
        break
    if checkTie(board):
      newgame = input("\nNew Game? Press Enter: ")
      if len(newgame) == 0:
        resetBoard(board)
      else:
        print("\nSee you soon!")
        break

    switchPlayer()
    
    computerEasy(board)
    if checkWinner():
      newgame = input("\nNew Game? Press Enter: ")
      if len(newgame) == 0:
        resetBoard(board)
      else:
        print("\nSee you soon!")
        break
    if checkTie(board):
      newgame = input("\nNew Game? Press Enter: ")
      if len(newgame) == 0:
        resetBoard(board)
      else:
        print("\nSee you soon!")
        break

# --- Medium Game Running ---
def mediumGame():
  while gameRunning:
    printGameBoard(board)

    playerInput(board)
    if checkWinner():
      newgame = input("\nNew Game? Press Enter: ")
      if len(newgame) == 0:
        resetBoard(board)
      else:
        print("\nSee you soon!")
        break
    if checkTie(board):
      newgame = input("\nNew Game? Press Enter: ")
      if len(newgame) == 0:
        resetBoard(board)
      else:
        print("\nSee you soon!")
        break

    switchPlayer()
    
    computerMedium(board)
    if checkWinner():
      newgame = input("\nNew Game? Press Enter: ")
      if len(newgame) == 0:
        resetBoard(board)
      else:
        print("\nSee you soon!")
        break
    if checkTie(board):
      newgame = input("\nNew Game? Press Enter: ")
      if len(newgame) == 0:
        resetBoard(board)
      else:
        print("\nSee you soon!")
        break

# --- Hard Game Running ---
def hardGame():
  while gameRunning:
    printGameBoard(board)

    playerInput(board)
    if checkWinner():
      newgame = input("\nNew Game? Press Enter: ")
      if len(newgame) == 0:
        resetBoard(board)
      else:
        print("\nSee you soon!")
        break
    if checkTie(board):
      newgame = input("\nNew Game? Press Enter: ")
      if len(newgame) == 0:
        resetBoard(board)
      else:
        print("\nSee you soon!")
        break

    switchPlayer()
    
    computerHard(board)
    if checkWinner():
      newgame = input("\nNew Game? Press Enter: ")
      if len(newgame) == 0:
        resetBoard(board)
      else:
        print("\nSee you soon!")
        break
    if checkTie(board):
      newgame = input("\nNew Game? Press Enter: ")
      if len(newgame) == 0:
        resetBoard(board)
      else:
        print("\nSee you soon!")
        break

# --- Hard Game Running ---
def impossibleGame():
  while gameRunning:
    printGameBoard(board)

    playerInput(board)
    if checkWinner():
      newgame = input("\nNew Game? Press Enter: ")
      if len(newgame) == 0:
        resetBoard(board)
      else:
        print("\nSee you soon!")
        break
    if checkTie(board):
      newgame = input("\nNew Game? Press Enter: ")
      if len(newgame) == 0:
        resetBoard(board)
      else:
        print("\nSee you soon!")
        break

    switchPlayer()
    
    computerImpossible(board)
    if checkWinner():
      newgame = input("\nNew Game? Press Enter: ")
      if len(newgame) == 0:
        resetBoard(board)
      else:
        print("\nSee you soon!")
        break
    if checkTie(board):
      newgame = input("\nNew Game? Press Enter: ")
      if len(newgame) == 0:
        resetBoard(board)
      else:
        print("\nSee you soon!")
        break

# --- Select the difficult ---
def selectDifficulty():
  difficult = input("\nSelect the difficult: [E]asy, [M]edium, [H]ard or [I]mpossible? ")
  clear()
  if difficult in easy:
    easyGame()
  elif difficult in medium:
    mediumGame()
  elif difficult in hard:
    hardGame()
  elif difficult in impossible:
    impossibleGame()
  else: 
    print("\nPlease, insert the correct difficulty!")
    selectDifficulty()

# --- Start the game ---
selectDifficulty()