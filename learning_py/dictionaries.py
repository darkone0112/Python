# dictionery = A collection which is unordered, changeable and indexed. No duplicate members, following this format: {key:value} 

capitals = {'USA':'Washington DC',
            'UK':'London',
            'France':'Paris',
            'Germany':'Berlin',
            'Italy':'Rome'}

# print(capitals['India']) this will be a key error if the key is not found in the dictionary
while True:
    print("_" * 50)
    print("What do you want to do?")
    print("1. Add a new country")
    print("2. Remove a country")
    print("3. Change the capital of a country")
    print("4. Print all countries and capitals")
    print("5. Show the capital of a country")
    print("6. Quit")
    switch = int(input("Enter your choice: "))
    if switch == 1:
        new_country = input("Enter the name of the new country: ")
        new_capital = input("Enter the capital of the new country: ")
        capitals[new_country] = new_capital
        print("The new country and capital have been added")
    elif switch == 2:
        remove_country = input("Enter the name of the country to remove: ")
        del capitals[remove_country]
        print("The country and capital have been removed")
    elif switch == 3:
        change_country = input("Enter the name of the country to change: ")
        change_capital = input("Enter the new capital of the country: ")
        capitals[change_country] = change_capital
        print("The capital of the country has been changed")
    elif switch == 4:
        print(capitals)
    elif switch == 5:
        show_country = input("Enter the name of the country to show the capital: ")
        country = capitals.get(show_country)
        if country == None:
            print("The country is not in the dictionary")
        else:
            print("The capital of " + show_country + " is " + country)
    elif switch == 6:
        print("Goodbye")
        break

