import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess the number between 1 and {x}: '))
        print(guess)
        
        if guess < random_number:
            print('sorry guess again, too low')
        elif guess > random_number:
            print("sorry, gues again. too high")
    
    print(f'yay, congrats. you have guess the random number {random_number} correctly')



guess(25)