# scope = THe region of a program where a variable is recognized as being defined and can be used to refer to a value or object

name = "Global" # global variable because it is defined outside of the function

def display_name():
    name = "Local" # local variable because it is defined inside the function
    print(name) #This will use the local variable first because it is defined inside the function

#print(name) # NameError: name 'name' is not defined because name is not defined outside of the function

print(name) # This will use the global variable because it is defined outside of the function

# This is called LEGB rule = Local, Enclosing, Global, Built-in = Local variables are searched first, then enclosing functions, then global variables, then built-in functions in that order
