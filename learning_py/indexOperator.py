# index operator [] is used to access the elements of a sequence (list, tuple, string)

name = input("Enter your name: ")

if(name[0].islower()):
    print("The first letter is lowercase")
    option = input("Do you want to capitalize it? (y/n): ")
    if option == "y":
        name = name.capitalize()
        print("Your name is now " + name)
    else:
        print("Your name is still " + name)

first_name = name[0:name.find(" ")].upper()
last_name = name[name.find(" "):].lower() 
last_character = len(last_name) - 1

print("Your first name is " + first_name)
print("Your last name is " + last_name)
print("The last character of your last name is " + last_name[last_character])