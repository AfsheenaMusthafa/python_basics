secret_code = "python"
while True:
    user_input = input("Enter secret code: ")
    if user_input == secret_code:
        print("Access granted!")
        break
    else:
        print("Wrong code! Try again.")
