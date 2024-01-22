
# for i in range(5):
#   print("i love Sampson")
# print("done")
# for i in range(99):
#    print(i+2)
# for i in range(2,102,2):
#    print(i)

# print("This program takes three integers and returns the sum.")
# total = 0
# for i in range(3):
#    x = input("Enter a number: ")
#    total += i
# print("The total is:", x)

# Write a program that will use a WHILE loop to count from 10 down to, and including, 0.
# Then print the words Blast off! Remember, use a WHILE loop, don't use a FOR loop.
# for i in range(10):
#    print(i)

# i = 10
# while i > -1:
#    print(i)
#    i -= 1


# i = 0
# while i < 10:
#    print(i)
#    i += 1

# Write a program that prints a random integer from 1 to 10 (inclusive). (5pts)
# import random
# my_number = random.randrange(1, 11)
# print(my_number)

# Ask the user for seven numbers finish
# * Print the total sum of the numbers finish
# * Print the count of the positive entries, the count of entries equal to zero,
# and the count of negative entries. Use an if, elif, else chain, not just three
# if statements.

for i in range(7):
    num = int(input("enter a number"))


# num_sum = num1 + num2 + num3 + num4 + num5 + num6 + num7
# print(num_sum)

# Create a program that will print a random 0 or 1.
# 2.) Instead of 0 or 1, print heads or tails. Do this using if statements. Don't select from a list.
# 3.) Add a loop so that the program does this 50 times.
# 4.) Create a running total for the number of heads and the number of tails and print the total at the end.

# import random
# my_number = random.randrange(0, 2)
# if my_number == 1:
#   print("tails")
# if my_number == 0:
#    print("Heads")

# var = 10
# while var > -1:
#    print(var)
#    var -= 1
#    if var == -1:
#        print("blast off!")

# print("This program takes three integers and returns the sum.")
#     total = 0
#     for i in range(3):
#         x = input("Enter a number: ")
#         total+=i
#     print("The total is:", x)

# print("This program takes three integers and returns the sum.")
# total = 0
# for i in range(3):
#    x = int(input("Enter number: "))
#    total += x
# print("The total is:", total)

# Create a program that randomly chooses a 1, 2, or 3.
# Expand the program, so it randomly prints rock, paper, or scissors using if statements. Don't select from a list.
# Add to the program, so it first asks the user their choice as well as if they want to quit.(1 for rock, 2 for paper, 3 for scissors and 4 for quit)
# I don't want to be asked to quit each time. I will enter a 4 if I want to quit.
# Add conditional statements to figure out who wins and keep the records
# Each round, tell me what the computer chose, what I chose and also if I won, lost or tied.
# When the user quits, print an end game message and their win/loss/tie record

import random
my_number = random.randrange(1, 4)  # this is a list need to be random using if statements
x = int(input("What do you choose? 1 for rock, 2 for paper, 3 for scissors, and finally 4 to quit"))
win = "you beat the computer and won"
tie = "You tied with the computer"
lost = "you lost the computer won"

# you choose rock
if x == 1 and my_number == 1:
    print("the computer choose rock", tie)

if x == 1 and my_number == 2:
    print("The computer choose paper", lost)

if x == 1 and my_number == 3:
    print("the computer choose scissors", win)

# you choose paper
if x == 2 and my_number == 1:
    print("the computer choose rock", lost)

if x == 2 and my_number == 2:
    print("The computer choose paper", tie)

if x == 2 and my_number == 3:
    print("the computer choose scissors", win)

# you choose scissors
if x == 3 and my_number == 1:
    print("the computer choose rock", lost)

if x == 3 and my_number == 2:
    print("The computer choose paper", win)

if x == 3 and my_number == 3:
    print("the computer choose scissors", tie)

# ends the game
# end of game must include a way keep track of win, loss, and tie record





