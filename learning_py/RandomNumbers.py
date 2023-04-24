import random

x = random.randint(1, 100)
y = random.random()

print(y)
print(x)

options = ["rock", "paper", "scissors"]
z = random.choice(options)
print(z)

cards = ["jack", "queen", "king", "ace"]

random.shuffle(cards)
print(cards)