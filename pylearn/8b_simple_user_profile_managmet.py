# Exercise 8c: Create a dictionary of user profiles.
# Each profile should store name (as key), and a dict with age and email as value.
# After all profiles are entered, show the full dictionary and let the user look up one name.

def profile_manager():
    # ↓↓↓ Write your code here ↓↓↓

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
