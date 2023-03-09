#Strings
name = "World"
print("Hello" + name)
full_hello = "Hello" + name
print("The dataType of name is" + type(name))
print(full_hello)

#numbers
age = 21
age += 1
print(age)
print("The dataType of age is" + type(age))

#Boolean
status = True;
if status:
    print("The status is true")
else:
    print("The status is false")
    
#Multiple assignment examples
def multiple_assignment():
    a, b, c = 1, 2, 3
    print(a)
    print(b)
    print(c)