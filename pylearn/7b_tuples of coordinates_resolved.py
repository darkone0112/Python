# Exercise 7b: Ask the user to enter X and Y coordinates (both float).
# Store them in a tuple.
# Then:
# - Print the tuple
# - Print X (the first element)
# - Print Y (the second element)

def coordinates_tuple(x,y):
    # ↓↓↓ Write your code here ↓↓↓
    tuple = (x,y)
    return tuple
    # ↑↑↑ Write your code here ↑↑↑
    pass  # remove this when you write your code

def run_coordinates_tuple():
    x = float(input("Enter float value for X: "))
    y = float(input("Enter float value for Y: "))
    tuple = coordinates_tuple(x,y)
    
    print(f"Tuple: {tuple}")
    print(f"X: {x}")
    print(f"Y: {y}")
    


# --- DO NOT EDIT BELOW THIS LINE ---
def run_test():
    print("Example: user types 10.5 and 20.3")
    print("Tuple: (10.5, 20.3)")
    print("X: 10.5")
    print("Y: 20.3")
    print("--- Now it's your turn ---")
    run_coordinates_tuple()

if __name__ == "__main__":
    run_test()
