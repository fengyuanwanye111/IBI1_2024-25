# Pseudocode:
# 1. Initialize a variable to store the current triangle number
# 2. Use a loop to calculate the sum from 1 to n for each n
# 3. Print the first 10 triangular numbers
#伪代码：
#1. 初始化一个变量来存储当前的三角形号
#2. 使用循环计算每个 n 从 1 到 n 的总和
#3. 打印前 10 个三角形数字

# Initialize variables
#初始化变量
n = 1
total = 0

# Loop to calculate the first 10 triangular numbers
#循环计算前 10 个三角形数
while n <= 10:
    total = total + n
    print(f"Triangle number T_{n} = {total}")
    n = n + 1