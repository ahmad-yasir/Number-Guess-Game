import random

print("-------// Number Guess Game \\\-------\n")
print("You will get four turns in total for predicting\n")
diff = input("Select Difficulty(easy/moderate/hard): ")

if diff == "easy":
    n = random.randint(1, 10)
    print("\nGuess between 1-10\n")
elif diff == "moderate":
    n = random.randint(1, 20)
    print("\nGuess between 1-20\n")
elif diff == "hard":
    n = random.randint(1, 40)
    print("\nGuess between 1-40\n")

wrong = 0
for i in range(4):
    guess = int(input("Enter your guess: "))

    if guess == n:
        print("Congrats! You have won the game.")
        break
    elif guess > n:
        print("Too Large.")
        wrong += 1
    elif guess < n:
        print('Too Small.')
        wrong += 1

if wrong == 4:
    print("\nGame Over!")
    print("Correct Number was:", n)
