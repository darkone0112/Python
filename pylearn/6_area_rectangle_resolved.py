# Exercise 6: Write a function `rectangle_area` that takes width and height (both floats)
# and returns the area (width * height).
# Then, ask the user for width and height, call the function, and print the result.

def rectangle_area(width, height):
    # ↓↓↓ Write your code here ↓↓↓
    area = width * height
    return area
    # ↑↑↑ Write your code here ↑↑↑
    pass  # remove this when you write your code

def run_rectangle_area(): 
    # ↓↓↓ Write your code here ↓↓↓
    width = float(input("Enter the width: "))
    height = float(input("Enter the height: "))
    area = rectangle_area(width, height)
    print(f"The rectangle area is: {area}")
    # ↑↑↑ Write your code here ↑↑↑
    pass  # remove this when you write your code

# --- DO NOT EDIT BELOW THIS LINE ---
def run_test():
    print("Example if user types 5 and 3: (we care about the logic, not format)")
    print("Expected area: 15.0")
    print("--- Now it's your turn ---")
    run_rectangle_area()

if __name__ == "__main__":
    run_test()
