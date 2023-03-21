#a for loop is a loop that is used to iterate over a sequence /
#(that is either a list, a tuple, a dictionary, a set, or a string). /
#This is less like the for keyword in other programming languages, /
#and works more like an iterator method as found in other object- /
#the diference with while loop is that the while loop runs as long /
#as the condition is true, while the for loop runs for a specific /
#number of times.

import time


for i in range (10):#range is a function that returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
    print(i + 1)

for i in range (50,100 + 1):#range can be used to iterate over a sequence of numbers
    print(i)
    
for i in "Javier Menendez": #for loop can be used to iterate over a string
    print(i)         
    
for seconds in range(10,0,-1): #for loop can be used to iterate over a sequence of numbers in reverse order
    print(seconds)
    time.sleep(1) 
print("Happy New Year!")  
