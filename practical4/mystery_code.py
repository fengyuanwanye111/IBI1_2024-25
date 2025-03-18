# What does this piece of code do?
# Answer: This code simulates rolling two six-sided dice until they show the same number and prints the number of rolls it took.

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5 (Note: ceil is imported but not used in this code)
from math import ceil

# Initialize progress to count the number of rolls
progress = 0

# Start a loop that continues until broken
while progress >= 0:
    # Increase the number of roll
    progress += 1
    # Roll the first dice (random number between 1 and 6)
    first_n = randint(1, 6)
    # Roll the second dice (random number between 1 and 6)
    second_n = randint(1, 6)
    # Check if the two dice show the same number
    if first_n == second_n:
        # Print the number of rolls it took 
        print(progress)
        # Exit the loop
        break