import random

print("Guess a number between 1 and 100! You have 7 tries!")
guess = int(input())
answer = random.randint(1, 100)
counter = 1

while(counter <= 6 and guess != answer):
    if(guess > 100 or guess < 1):
        print("You guessed outside the range! Try again!")
    elif (guess > answer):
        print("Your guess of", guess, "was too high!")
    else:
        print("Your guess of", guess, "was too low!")
    print("Try again!")
    guess = int(input())
    counter += 1

if(counter == 7 and guess != answer):
    print("You ran out of guesses!", answer, "was the correct answer!")
    
else:
    print("Your guess of", guess, "was correct!")
    