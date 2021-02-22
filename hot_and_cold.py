import random

guesses = []

m = random.randint(1,10)   # row of the target
n = random.randint(1,10)   # column of the target
target = m,n

warm_i = range(m-1, m+2) if m>1 and m<10 else range(max(2, m)-1, min(9,m)+2)
warm_j = range(n-1, n+2) if n>1 and n<10 else range(max(2, n)-1, min(9,n)+2)

mines = []
num_mines = 4
while len(mines)!= num_mines:
    mine = random.randint(1,10), random.randint(1,10)
    if mine not in mines and (mine[0] not in warm_i or mine[1] not in warm_j):
        mines.append(mine)

def board(target, warm_i, warm_j, mines, guesses, end):
    for x in range(1, 11):    # first row of 1 to 10
        if x == 1:
            print("  ", x, end="  ")
        else:
            print(x, end="  ")
    print("")
    for i in range(1, 11):
        if i == 10:           # column from 1 to 10
            print(i, end=" ")
        else:
            print(i, end="  ")

        for j in range(1, 11):
            if end and i == target[0] and j == target[1]:
                print("$", end="  ")
            elif end and (i,j) in mines:
                print("X", end="  ")
            elif (end or (i,j) in guesses) and i in warm_i and j in warm_j:
                print("+", end="  ")
            elif (i,j) in guesses:
                print("-", end="  ")
            else:
                print("*", end="  ")
        print("")
    return ""

def valid_guess(guess):
    try:
        guess = guess.split(",")
        x, y = int(guess[0]), int(guess[1])
    except:
        return False
    else:
        return True if len(guess)== 2 and x in range(1,11) and y in range(1,11) else False

def terminate(guess):
    return guess in mines or guess == target

def user_guess():
    while True:
        guess = input("Where is the target? Input the row number, ',' and the column number: ")
        if valid_guess(guess):
            guess = guess.split(",")
            guess = int(guess[0]), int(guess[1])
            guesses.append(guess)
            return guess
        else:
            print("Invalid guess. Try again.")

print("Let's start the game!")
print("On the board below, there are", num_mines, "mines (X), a target ($) and (+) when you get closer to the target.\n")
print(board(target, warm_i, warm_j, mines, guesses, False))

while True:
    x = user_guess()
    print(board(target, warm_i, warm_j, mines, guesses, terminate(x)))
    if x == target:
        print("Congratulations! You win! \nIt took you", len(guesses), "tries.")
        break
    elif x in mines:
        print("Game over!")
        break
    elif x in guesses[:-1]:
        print("You already guessed this position. Try another guess!")
    else:
        print("Try another guess!")