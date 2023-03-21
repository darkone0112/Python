name = "name"

#some examples of string methods
def string_methods():
    #capitalize
    print(name.capitalize())
    #center
    print(name.center(10))
    #count
    print(name.count("n"))
    #endswith
    print(name.endswith("e"))
    #find
    print(name.find("n"))
    #index
    print(name.index("n"))
    #isalnum
    print(name.isalnum())
    #isalpha
    print(name.isalpha())
    #isdigit
    print(name.isdigit())
    #islower
    print(name.islower())
    #isupper
    print(name.isupper())
    #isspace
    print(name.isspace())
    #istitle
    print(name.istitle())
    #join
    print(name.join("a"))
    #lower
    print(name.lower())
    #upper
    print(name.upper())
    #lstrip
    print(name.lstrip())
    #rstrip
    print(name.rstrip())
    #strip
    print(name.strip())
    #replace
    print(name.replace("n", "m"))
    #split
    print(name.split("n"))
    #title
    print(name.title())
    #swapcase
    print(name.swapcase())
    #zfill
    print(name.zfill(10))
    
# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    string_methods()