#random
#seq in general means a list
#flip a coin in python
import random # this gives access to all the functions in that particular library
coin=random.choice(['heads', 'tails']) # this will randomly choose between heads and 
print(coin)

#from random import choice
#random.randint(a,b)
number = random.randint(1,10)
print(number)
#random.shuffle(x)
cards=["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
   print(card)