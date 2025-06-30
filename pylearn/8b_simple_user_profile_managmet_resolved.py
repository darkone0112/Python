# Exercise 8c: Create a dictionary of user profiles.
# Each profile should store name (as key), and a dict with age and email as value.
# After all profiles are entered, show the full dictionary and let the user look up one name.

def profile_manager():
    # ↓↓↓ Write your code here ↓↓↓
    profiles = {}
    exit = False
    i = 0
    while exit == False:
        print(exit)
        i += 1
        name = input(f"Enter {i}º name: ")
        age = int(input(f"Enter {name}´s age: "))
        email = input(f"Enter {name}´s email address: ")
        profiles[name] = {'age' : age, 'email' : email}
        status = input("If there are no more names to be added writte exit: ").lower()
        print(status)
        if status == "exit":
            exit = True
        else:
            exit = False
            
    run_profile_manager(profiles)
    
    

def run_profile_manager(profiles):
    print(f"The full profiles list is: {profiles}")
    option = None
    while option not in profiles:
        option = input("Select a profile by name to show details: ").lower()
        if option not in profiles:
            print("Cannot find that name in the dictionary !!")
    print(f"The selected profile is: {option}: his/her age is: {profiles[option]['age']} and the assigned email is: {profiles[option]['email']}")
    # ↑↑↑ Write your code here ↑↑↑
    pass  # remove this when done

# --- DO NOT EDIT BELOW THIS LINE ---
def run_test():
    print("Example:")
    print("How many profiles? 2")
    print("Name: Alice | Age: 30 | Email: alice@x.com")
    print("Name: Bob | Age: 22 | Email: bob@x.com")
    print("Dictionary: {'Alice': {'age': 30, 'email': 'alice@x.com'}, ...}")
    print("Enter name to look up: Bob")
    print("Result: age = 22, email = bob@x.com")
    print("--- Now it's your turn ---")
    profile_manager()

if __name__ == "__main__":
    run_test()
