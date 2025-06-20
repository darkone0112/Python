# Exercise 5: Ask the user for a positive integer.
# Print numbers counting down from that number to 1.
# Example: If user enters 3, output:
# 3
# 2
# 1

def countdown():
    # ↓↓↓ Write your code here ↓↓↓
    n = int(input("Enter a countdown value: "))
    
    for i in range(n):
        print(n - i)
        
    # ↑↑↑ Write your code here ↑↑↑
    #pass  # remove this when you write your code

# --- DO NOT EDIT BELOW THIS LINE ---
def run_test():
    print("Example if user types 3: (we care about the logic, not format)")
    print("3\n2\n1")
    print("--- Now it's your turn ---")
    countdown()

if __name__ == "__main__":
    run_test()
