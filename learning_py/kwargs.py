# **kwargs = parameter that will pack all arguments into a dictionary

def hello(**kwargs): # **kwargs = parameter that will pack all arguments into a dictionary, the name kwargs is a convention, you can name it anything you want but kwargs is the most common
    print("Hello " + kwargs["first"] + " " + kwargs["middle"] + " " + kwargs["last"]) # This will print the values of the arguments passed to the function
    
    for key, value in kwargs.items():# This will print the key and value of the arguments passed to the function
        print(key + " = " + value)# This will print the key and value of the arguments passed to the function
    
hello(last="Smith",first="John",middle="Paul")