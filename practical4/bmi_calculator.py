# Pseudocode:
# 1. Prompt user to input weight (kg) and height (m)
# 2. Convert inputs to float for calculation
# 3. Calculate BMI using the formula: BMI = weight / (height^2)
# 4. Compare BMI with thresholds (underweight < 18.5, normal 18.5-30, obese > 30)
# 5. Print the BMI and weight category

# Prompt user for input
weight = float(input("Enter your weight in kg: "))  # Get weight from user
height = float(input("Enter your height in meters: "))  # Get height from user

# Calculate BMI
bmi = weight / (height ** 2)

# Determine weight category
if bmi < 18.5:
    category = "underweight"
elif 18.5 <= bmi <= 30:
    category = "normal weight"
else:
    category = "obese"

# Print result
print("Your BMI is " + str(bmi) + ". You are considered " + category + ".")