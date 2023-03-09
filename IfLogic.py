age = int(input("How old are you? "))
if age < 18:
    print("You are not old enough to vote")
elif age >= 18:
    print("You are old enough to vote")
else:
    print("Cannot determine your age")