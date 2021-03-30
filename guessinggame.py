#number guessing game
import random
import time


broj=random.randint(0,10)

tries=int(input("Enter number of tries "))
if tries>5: print("Wow you're really not good at guessing xD")
time.sleep(2)
pbroj=int(input("Guess the number ranging from 0-10 "))


if pbroj<broj: print("Guess higher ")
if pbroj>broj: print("Guess lower ")

while pbroj != broj and tries<tries:
    pbroj=int(input("Try again "))
    if pbroj < broj: print("Guess lower ")
    if pbroj > broj: print("Guess higher ")

if pbroj==broj: print("Go pogodivte brojot " + str(broj))
else: print(f"You lose the game with {tries} tries and the number you couldnt guess was {broj}")
