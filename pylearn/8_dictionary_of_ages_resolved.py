# Exercise 8a: Create an empty dictionary.
# Ask the user to enter 3 names and their ages (name: str, age: int).
# Store them in the dictionary with the name as the key and age as the value.
# Then:
# - Print the full dictionary
# - Print the age of the first entered name

def age_dictionary():
    # ↓↓↓ Write your code here ↓↓↓
    profiles = {}
    for i in range(3):
        name = input(f"Enter {i+1}º name: ")
        age = int(input(f"Enter {name} age: "))
        profiles[name] = age
    
    run_age_dictionary(profiles)
    # ↑↑↑ Write your code here ↑↑↑
    

def run_age_dictionary(profiles):
    first_key = list(profiles.keys())[0]
    print(f"Dict: {profiles}")
    print(f"The first entry is: {first_key}, his/her age is: {profiles[first_key]}")


# --- DO NOT EDIT BELOW THIS LINE ---
def run_test():
    print("Example: user types Alice 30, Bob 25, Carol 22")
    print("Dict: {'Alice': 30, 'Bob': 25, 'Carol': 22}")
    print("Age of Alice: 30")
    print("--- Now it's your turn ---")
    age_dictionary()

if __name__ == "__main__":
    run_test()
