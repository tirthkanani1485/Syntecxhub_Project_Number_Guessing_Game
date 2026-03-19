from random import randint

best_Score = None

def Number_guessing_game():
    global best_score

    print("\nSelect Difficulty Level:")
    print("1. Easy (1 to 50)")
    print("2. Medium (1 to 100)")
    print("3. Hard (1 to 200)")

    choice = input("Enter choice (1/2/3): ")

    if choice == "1":
        low, high = 1, 50
    elif choice == "2":
        low, high = 1, 100
    elif choice == "3":
        low, high = 1, 200
    else:
        print("Invalid choice, defaulting to Medium.")
        low, high = 1, 100

    num = randint(low, high)
    attempts = 0

    print(f"\nGuess the number between {low} and {high}")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < num:
                print("Too low! Try again.")
            elif guess > num:
                print("Too high! Try again.")
            else:
                print(f"🎉 Correct! You guessed in {attempts} attempts.")

                if best_score is None or attempts < best_score:
                    best_score = attempts
                    print("🏆 New Best Score!")

                print(f"Best Attempts: {best_score}")
                break

        except ValueError:
            print("Please enter a valid number.")

while True:
    Number_guessing_game()
    
    again = input("\nDo you want to play again? (y/n): ").lower()
    if again != 'y':
        print("Thanks for playing! 👋")
        break