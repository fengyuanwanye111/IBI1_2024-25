# What does this piece of code do?
# Answer: This code simulates rolling two six-sided dice until they show the same number and prints the number of rolls it took.

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5

#这段代码有什么作用？
# 答案：此代码模拟滚动两个六面骰子，直到它们显示相同的数字并打印它所花费的滚动次数。
#导入库
#randint 允许绘制随机数，
# 例如 randint（1,5）绘制一个介于 1 和 5 之间的数字
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5 (Note: ceil is imported but not used in this code)
#ceil 取一个数字的上限，即下一个更高的整数。
# 例如 ceil（4.2）=5（注意：ceil 已导入但未在此代码中使用）
from math import ceil

# Initialize progress to count the number of rolls
#初始化进度以计算卷数
progress = 0

# Start a loop that continues until broken
#开始一个循环，一直持续到断开
while progress >= 0:
    # Increase the number of roll
    # 增加卷数
    progress += 1
    # Roll the first dice (random number between 1 and 6)
    # 掷第一个骰子（1 到 6 之间的随机数）
    first_n = randint(1, 6)
    # Roll the second dice (random number between 1 and 6)
    # 掷第二个骰子（1 到 6 之间的随机数）
    second_n = randint(1, 6)
    # Check if the two dice show the same number
    # 检查两个骰子是否显示相同的数字
    if first_n == second_n:
        # Print the number of rolls it took 
        # 打印它需要的卷数
        print(progress)
        # Exit the loop
        # 退出循环
        break