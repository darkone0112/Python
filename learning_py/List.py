#list is a collection which is ordered and changeable. Allows duplicate members.

food = ["pizza", "hamburger", "kebab", "pollon"]

print(food)#prints the list
print(food[0])#prints the first item in the list
print("_________________________")
for i in food: #for loop can be used to iterate over a list
    print(i)
    
food.append("pasta")#adds an item to the end of the list
food.remove("pizza")#removes the specified item
food.pop(0)#removes the specified index
food.insert(0, "cake")#adds an item at the specified index
food.sort()#sorts the list
food.clear()#removes all the elements from the list