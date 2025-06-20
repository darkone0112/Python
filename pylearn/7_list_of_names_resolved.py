# Exercise 7: Ask the user to enter 3 names (one by one) and store them in a list.
# Then:
# - Print the full list
# - Print the first name in the list
# - Print the list length

def names_list():
    # ↓↓↓ Write your code here ↓↓↓
    name_list = []
    for i in range(3):
        name_list.append(input(f"Enter {i+1}º name: "))
    
    return name_list
        
def run_name_list():
    name_list = names_list()
    print(f"Full list: {name_list}")
    print(f"The first name is: {name_list[0]}")
    print(f"The lenght of the list is: {len(name_list)}")
        
    # ↑↑↑ Write your code here ↑↑↑
    #pass  # remove this when you write your code

# --- DO NOT EDIT BELOW THIS LINE ---
def run_test():
    print("Example: user types Alice, Bob, Carol")
    print("Full list: ['Alice', 'Bob', 'Carol']")
    print("First name: Alice")
    print("List length: 3")
    print("--- Now it's your turn ---")
    run_name_list()

if __name__ == "__main__":
    run_test()
