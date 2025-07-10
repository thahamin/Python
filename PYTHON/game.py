secret_number = 5
guess_count = 1
guess_linit = 3

while guess_count <= guess_linit :
    user_guess_number = int(input("guess> "))
    guess_count += 1
    if user_guess_number == secret_number:
        print("you win")
        break
else:
    print("you lose :( ")    