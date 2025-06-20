# Exercise 4: Ask the user for an integer.
# Print:
# "Positive" if the number is greater than 0
# "Negative" if the number is less than 0
# "Zero" if the number is 0

def number_sign_checker():
    # ↓↓↓ Write your code here ↓↓↓

    n = int(input("Enter an Integer: "))
    
    if n > 0:
        print("Positive!")
    elif n < 0:
        print("Negative")
    else:
        print("The number is zero")

    # ↑↑↑ Write your code here ↑↑↑
    #pass  # remove this when you write your code

# --- DO NOT EDIT BELOW THIS LINE ---
def run_test():
    print("Expected output if user types 5: Positive")
    print("Expected output if user types -3: Negative")
    print("Expected output if user types 0: Zero")
    print("--- Now it's your turn ---")
    number_sign_checker()

if __name__ == "__main__":
    run_test()