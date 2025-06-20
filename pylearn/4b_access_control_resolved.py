# Exercise 4b: Ask the user for their age (int) and password (str).
# Conditions:
# - If age >= 18 AND password is "opensesame": print "Access granted"
# - If age >= 18 AND password is wrong: print "Wrong password"
# - If age < 18 OR age is exactly 0: print "Access denied - underage"
# - If age < 0: print "Invalid age"
# Use nested ifs or combined conditions where appropriate.

def access_control():
    # ↓↓↓ Write your code here ↓↓↓
    age = int(input("Enter your age:"))
    password = input("Enter your password: ")
    
    if age >= 0:
        if age >= 18 and password == "opensesame":
            print("Access Granted")
        elif password != "opensesame":
            print("Wrong Password")
        elif age < 18:
            print("Access Denied - underage")
    
    else:
        print("Invalid number")
    
    # ↑↑↑ Write your code here ↑↑↑
    pass  # remove this when you write your code

# --- DO NOT EDIT BELOW THIS LINE ---
def run_test():
    print("Examples of correct outputs:")
    print("If age 20, password opensesame: Access granted")
    print("If age 20, password wrong: Wrong password")
    print("If age 15, password anything: Access denied - underage")
    print("If age 0, password anything: Access denied - underage")
    print("If age -1, password anything: Invalid age")
    print("--- Now it's your turn ---")
    access_control()

if __name__ == "__main__":
    run_test()
