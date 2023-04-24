# exception = events detected during execution that interrupt the normal flow of a program and cause it to crash or terminate
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    result = numerator / denominator
except ZeroDivisionError as e:
    print("Cannot divide by zero!")
    print(e)
except ValueError as e:
    print("Numerator and denominator must be valid numbers!")
    print(e)
except Exception as e:
    print("Something went wrong!")
    print(e)
else:
    print(result)
finally:
    print("Finished.")