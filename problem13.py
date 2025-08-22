import random
def main():
    greeting = input("Hello! What is your name? ")
    print(f"Well, {greeting}, I am thinking of a number between 1 and 20. \n Take a guess.")
    random_int = random.randint(1, 20)
    guess = None
    count = 0
    while guess != random_int:
        guess = int(input())
        count += 1
        if guess < random_int:
            print("Your guess is too low.")
        elif guess > random_int:
            print("Your guess is too high.")


    print(f"Good job, {greeting}! You guessed my number in {count} guesses!")



main()