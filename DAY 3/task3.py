
secret = 7
tries = 0

while True:
    guess = int(input("Guess the number (1-10): "))
    tries = tries + 1

    if guess == secret:
        print("Correct! You won in", tries, "tries.")
        break
    elif guess < secret:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

