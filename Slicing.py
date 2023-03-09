name = "Hello World"
hello = name[0:5]
world = name[6:11]
reverse = name[::-1]
print(hello + " " + world)
print(reverse)

#Slice Function
website = "http://www.google.com"
slice = slice(11, -4)
website = website[slice]
print(website)