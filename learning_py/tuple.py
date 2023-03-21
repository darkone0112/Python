#tuple is a collection which is ordered and unchangeable. Allows duplicate members. 

student = ("pepe",21,"male")#tuple is created using parenthesis

print(student.count("pepe"))#returns the number of times a specified value occurs in a tuple
print(student.index("male"))#searches the tuple for a specified value and returns the position of where it was found

for i in student:#for loop can be used to iterate over a tuple
    print(i)
    
if "pepe" in student:#to determine if a specified item is present in a tuple use the in keyword
    print("pepe is in the tuple")