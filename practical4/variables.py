# Walk to bus stop: 15 mins
a = 15
# Bus journey: 1 hr 15 mins = 75 mins
b = 75
# Total time for bus commute
c = a + b

# Drive: 1 hr 30 mins = 90 mins
d = 90
# Walk from car park: 5 mins
e = 5
# Total time for car commute
f = d + e

# Compare c and f: Which is shorter?
# c = 90 mins, f = 95 mins, so walking + bus is quicker
print("Bus commute time:", c, "mins")
print("Car commute time:", f, "mins")
# Section 4.2: Working with Booleans

# Initialize boolean variables
X = True
Y = False

# Create W as the logical AND of X and Y
W = X and Y

# Truth table for W (X and Y):
# X = True, Y = True  -> W = True
# X = True, Y = False -> W = False
# X = False, Y = True -> W = False
# X = False, Y = False -> W = False
print("W =", W)  # Output: False