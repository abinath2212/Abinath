import random

def play_game():
    print("=" * 40)
    print("Welcome to the Number Guessing Game!")
    print("=" * 40)
   
    # Generate random number between 1 and 100
    secret = random.randint(1, 100)
    attempts = 0
    max_attempts = 7
   
    print(f"\nI'm thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it!\n")
   
    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts} - Enter your guess: "))
            attempts += 1
           
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100!\n")
                attempts -= 1
                continue
           
            if guess == secret:
                print(f"\n🎉 Congratulations! You guessed it in {attempts} attempts!")
                print(f"The number was {secret}!\n")
                return True
            elif guess < secret:
                print("Too low! Try a higher number.\n")
            else:
                print("Too high! Try a lower number.\n")
               
        except ValueError:
            print("Invalid input! Please enter a number.\n")
            attempts -= 1
   
    print(f"\n💀 Game Over! You've used all {max_attempts} attempts.")
    print(f"The secret number was {secret}.\n")
    return False

def main():
    while True:
        play_game()
       
        play_again = input("Would you like to play again? (yes/no): ").lower()
        if play_again not in ['yes', 'y']:
            print("\nThanks for playing! Goodbye! 👋")
            break
        print("\n")

if __name__ == "__main__":
    main()
