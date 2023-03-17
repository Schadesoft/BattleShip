import random

# create the board
board = []
for i in range(10):
    board.append(["O"] * 10)

# randomly place the ships
ship_positions = []
for i in range(5):
    x = random.randint(0, 9)
    y = random.randint(0, 9)
    ship_positions.append((x, y))
    board[x][y] = "S"

# print the board
def print_board(board):
    for row in board:
        print(" ".join(row))

print("Let's play Battleship!")
print_board(board)

# opponent A.I. makes educated guesses
def opponent_guess(board, guesses):
    possible_targets = []
    for guess in guesses:
        x, y = guess
        if x > 0:
            possible_targets.append((x-1, y))
        if x < 9:
            possible_targets.append((x+1, y))
        if y > 0:
            possible_targets.append((x, y-1))
        if y < 9:
            possible_targets.append((x, y+1))
    target = random.choice(possible_targets)
    return target

# main game loop
guesses = []
while True:
    # player's turn
    guess = input("Guess a position (e.g. 'A5'): ")
    x = ord(guess[0].upper()) - 65
    y = int(guess[1]) - 1
    if (x, y) in guesses:
        print("You already guessed that position. Try again.")
        continue
    guesses.append((x, y))
    if board[x][y] == "S":
        print("Congratulations! You sunk one of the opponent's ships!")
        board[x][y] = "X"
    else:
        print("Sorry, that's a miss.")
    print_board(board)
    if all([board[x][y] != "S" for x, y in ship_positions]):
        print("Congratulations! You won!")
        break
    # opponent's turn
    target = opponent_guess(board, guesses)
    if board[target[0]][target[1]] == "S":
        print("The opponent sunk one of your ships!")
        board[target[0]][target[1]] = "X"
    else:
        print("The opponent missed.")
    print_board(board)
    if all([board[x][y] != "S" for x, y in ship_positions]):
        print("Sorry, you lost. The opponent won.")
        break
