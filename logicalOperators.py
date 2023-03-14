temp = int(input("What is the temperature?"))

if temp >= 0 and temp <= 30:
    print("Good weather")
    print("Go outside")
elif temp < 0 or temp > 30:
    print("Bad weather")
    print("Stay inside")
    
#With not operator you cold write inverse of the above