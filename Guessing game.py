import random

def play_game():
    top_of_range = input("Enter the top of the range: ")

    if top_of_range.isdigit():
        top_of_range = int(top_of_range)
        if top_of_range <= 0:
            print("please type a number larger than 0 next time")
            quit()
    else:
        print("Sorry but you have to input numbers")
        quit()

    random_number = random.randint(0, top_of_range)

    guesses = 0

##print("Your random number is " + str(random_number))

    while True:
        user_guess = input("Make a guess: ")
        if user_guess.isdigit():
            user_guess = int(user_guess)
            guesses += 1
        else:
            print("Sorry but you have to input numbers")
            continue
        if user_guess == random_number:
            print("YOU GOT IT")
            print("You got it in", guesses, "guesses")
            break
        elif user_guess > random_number:
            print("your guess is higher than the number")
        else:
            print("your guess is lower than the number")

play_game()

while True:
    play_again = input("Do you want to play again? (yes/no) ")
    if play_again.lower() == "yes":
        play_game()
    elif play_again.lower() == "no":
        print("Thanks for playing!")
        break
    else:
        print("Please enter 'yes' or 'no'.")