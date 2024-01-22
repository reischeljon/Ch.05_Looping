'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book

'''
import random

miles_traveled = 0
thirst = 0
tauntaun_tired = 0
empire_distance = -20
canteen_drinks = 3

# Instructions for game
print("Welcome to my camel game!")
print("In my game version you are Han solo in Star Wars the Empire Strikes Back!")
print("As Han solo you must ride your tauntaun across Hoth to save Luke he is currently 200 miles away.")
print("you must take care of your tauntaun and your health. As you must monitor it throughout your journey.")
print("There are random events throughout your journey, as they could change the course of your journey through Hoth.")
print("Are you up to the challenge? Or will the probe droid find you and report the rebel base to the Empire and arrest you?")

done = False
while not done:
    frozen_cave = 0
    print("\nA. Drink from your canteen.")
    print("B. Ahead moderate speed.")
    print("C. Ahead full speed")
    print("D. Stop for the night")
    print("E. Status check")
    print("Q. Quit")
    user_input = input("Please enter your choice Solo: ")

    if frozen_cave == 17:
        thirst = 0
        canteen_drinks = 3
        tauntaun_tired = 0
        print("You found a frozen cave! You refilled your canteen and your tauntaun took a rest.")

    if user_input.upper() == "Q":  # Quit the game
        done = True

    elif user_input.upper() == "A":  # Drink from canteen
        if canteen_drinks > 0:
            canteen_drinks = canteen_drinks - 1
            thirst = 0
            print("You feel refreshed Solo.")
        else:
            print("You have nothing to drink fool!")

    elif user_input.upper() == "B":  # Ahead moderate speed
        traveled = random.randrange(5, 12)
        miles_traveled += traveled
        print("You have traveled", traveled, "miles.")
        thirst += 1
        tauntaun_tired += 1
        empire_distance += random.randrange(7, 15)
        frozen_cave = random.randrange(1, 21)

    elif user_input.upper() == "C":  # Ahead full speed
        traveled = random.randrange(10, 21)
        miles_traveled += traveled
        print("You have traveled", traveled, "miles.")
        thirst += 1
        tauntaun_tired += random.randrange(1, 4)
        empire_distance += random.randrange(7, 15)

    elif user_input.upper() == "D":  # Stop for the night
        tauntaun_tired = 0
        print("Your tauntaun is rested and happy. :)")
        empire_distance += random.randrange(7, 15)

    elif user_input.upper() == "E":  # Status check
        print("Miles traveled:", miles_traveled)
        print("Drinks in canteen:", canteen_drinks)
        print("The probe droid is", miles_traveled-empire_distance, "behind you!")

    if thirst > 6:  # You died of thirst
        print("You have died of thirst you fool.")
        done = True
    elif thirst > 4 and not done:  # Your getting thirsty
        print("You are thirsty Solo.")

    if tauntaun_tired > 8:  # Tauntaun died of tired
        print("You fool! Your tauntaun has died.")
        done = True
    if tauntaun_tired > 5 and not done:  # Tauntaun getting tired
        print("Your tauntaun is getting tired.")

    distance_between = miles_traveled - empire_distance

    if distance_between <= 0:  # You got caught by the Empire
        print("Oh no you were caught by the probe droid and arrested! The empire found Hoth's base and Luke died!")
        done = True
    elif distance_between < 15 and not done:  # The Empire is getting closer
        print("The probe droid is getting closer!")

    if miles_traveled > 200:
        print("You win! You have rescued Luke Skywalker")
        done = True
