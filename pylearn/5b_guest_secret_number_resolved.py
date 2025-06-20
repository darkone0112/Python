# Exercise 5b: Set a secret number in your code (e.g., 7).
# Keep asking the user to guess the number (int) until they get it right.
# After each wrong guess, print: "Try again"
# When correct, print: "Correct! You guessed it."

def guess_secret_number():
    # ↓↓↓ Write your code here ↓↓↓
    secret = 7
    n = None
    while n != secret:
        n = int(input("Guess the number: "))
        if n != secret:
            print("Wrong number, Try again!")
        else:
            print("Correct! You guessed it.")
    
    # ↑↑↑ Write your code here ↑↑↑
    pass  # remove this when you write your code

# --- DO NOT EDIT BELOW THIS LINE ---
def run_test():
    print("Example run: (assume secret is 7)")
    print("User types 3: Try again")
    print("User types 5: Try again")
    print("User types 7: Correct! You guessed it.")
    print("--- Now it's your turn ---")
    guess_secret_number()

if __name__ == "__main__":
    run_test()
