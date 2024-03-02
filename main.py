import random

user = input("Enter your name: ")
print(f"Welcome {user}, Are you ready to play with me?")
machine_lives = int(input("Enter the desired lives of the machine: "))
lives = int(input("Enter your lives: "))

while lives > 0 and machine_lives > 0:
    try:
        user_input = int(input("Select your move \n 1-Rock \n 2-Paper \n 3-Scissors \n Your move:  "))
        if 1 <= user_input <= 3:
            random_choice = random.randint(1, 3)
            if user_input == random_choice:
                print("Draw")
            elif user_input > random_choice:
                machine_lives -= 1
                print("You won")
            else:
                lives -= 1
                print("You lost")
            print(f"Your lives: {lives}, Machine's lives: {machine_lives}")
        else:
            print("Wrong choice! Please enter a number between 1 and 3.")
    except ValueError:
        print("Invalid input! Please enter a valid number.")

if lives > machine_lives:
    print("Congratulations! You won.")
elif lives < machine_lives:
    print("Sorry, you lost. Better luck next time.")
else:
    print("It's a draw.")
