# Pseudocode:
# 1. Prompt user to input weight (kg) and height (m)
# 2. Convert inputs to float for calculation
# 3. Calculate BMI using the formula: BMI = weight / (height^2)
# 4. Compare BMI with thresholds (underweight < 18.5, normal 18.5-30, obese > 30)
# 5. Print the BMI and weight category

#伪代码：
#1.提示用户输入体重（kg）和身高（m）
#2.将输入转换为浮点数进行计算
#3.使用公式计算BMI：BMI=体重/（身高^2）
#4.将BMI与阈值（体重不足<18.5，正常18.5-30，肥胖>30）进行比较
#5.打印BMI和体重类别

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