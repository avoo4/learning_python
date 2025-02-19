# An extremely basic Russian Roulette game!
import random
import time
import sys


username = input("Please enter your username: ")
print(f"Welcome to russian roulette {username}(q to quit).")

def russian(hits, misses):
    chamber_rounds = ["Hit", "Miss"]
    shoot = random.choices(chamber_rounds, weights=[hits, misses], k=1)
    for x in shoot:
        if x == 'Miss':
            print("Loading", end=""); time.sleep(1); print(".", end=""); time.sleep(1); print(".", end=""); time.sleep(1); print("."); time.sleep(1)
            print("Congratulations partner! You have lived to see another day!")
        elif x == 'Hit':
            print("Loading", end=""); time.sleep(1); print(".", end=""); time.sleep(1); print(".", end=""); time.sleep(1); print("."); time.sleep(1)
            print("Hey, at the end of the day we all die, yours was just a bit sooner.")
        else:
            sys.exit("Error.")

while True:
    hits = input("How many bullets would you like to load?: ")
    misses = input("How many blanks would you like to load?: ")
    russian(hits, misses)
