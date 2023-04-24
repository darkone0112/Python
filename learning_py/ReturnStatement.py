# retur statement = Function returns a value to the caller of the function and terminates the function call

def multiply(num1, num2):
    result = num1 * num2
    return result

input1 = int(input("Enter first number: "))
input2 = int(input("Enter second number: "))
print(multiply(input1, input2))