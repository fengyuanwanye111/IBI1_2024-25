# Pseudocode:
# 1. Initialize a variable to store the current triangle number
# 2. Use a loop to calculate the sum from 1 to n for each n
# 3. Print the first 10 triangular numbers

# Initialize variables
n = 1
total = 0

# Loop to calculate the first 10 triangular numbers
while n <= 10:
    total = total + n
    print(f"Triangle number T_{n} = {total}")
    n = n + 1