#Loop COntrol Statement change the flow of execution of a loop by altering the way the loop is executed.
#break statement is used to exit a loop
#continue statement is used to skip the current iteration of a loop
#pass statement is used to do nothing

#break statement
while True:
    name = input("Enter your name: ")
    if name == "your name":
        break

#continue statement
phone_numeber = "123-456-7890"

for i in phone_numeber:
    if i == "-":
        continue
    print(i, end="")

#pass statement
for i in range(1, 21):
    if i == 13:
        pass
    else:
        print(i)