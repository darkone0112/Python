#2D list is a list that contains other lists
drinks = ["water", "juice", "soda"]
dinner = ["pizza", "hamburger", "kebab"]
dessert = ["ice cream", "chocolate", "candy"]

food = [drinks, dinner, dessert]

print(food)
print("1º List " + str(food[0]))

print("1º list second item is " + str(food[0][1]))