# *args = parameter that will pack all arguments into a tuple 

""" def add(num1,num2):
    sum = num1 + num2
    return sum """ #This will not work because we are only passing 2 arguments and the function is expecting 2 arguments 
    
def add (*args): # *args = parameter that will pack all arguments into a tuple, the name args is a convention, you can name it anything you want but args is the most common
    sum = 0
    args = list(args) # convert the tuple into a list so we can use the list methods on it
    args[0] = 10 # change the first element in the list to 10
    for i in args:
        sum += i
    return sum

print(add(1,2,3))