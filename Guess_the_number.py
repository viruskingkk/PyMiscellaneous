import random

number = random.randrange(1, 100)
running = True

while running:
    guess = int(input("Guess a number(1~100):"))

    if guess == number:
        print ("Congratulations! You win!")
        running = False

    elif guess < number:
        print ("Too small! :(")

    else:
        print ("Too big! :(")