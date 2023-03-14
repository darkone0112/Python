row = int(input("How many rows? "))
column = int(input("How many columns? "))
symbol = input("Enter a symbol to use: ")

for i in range (row):
    for j in range (column):
        print (symbol, end="")
    print()