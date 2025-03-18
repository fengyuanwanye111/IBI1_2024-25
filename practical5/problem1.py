# Pseudocode / 伪代码：
# 1. Create a dictionary with language data / 创建一个包含语言数据的字典
# 2. Print the dictionary / 打印字典
# 3. Use matplotlib to draw a bar chart / 用 matplotlib 画柱状图
# 4. Define a variable for input language and print its percentage / 定义输入语言变量并打印百分比

import matplotlib.pyplot as plt

# Step 1: Create dictionary / 创建字典
lang_popularity = {
    "JavaScript": 62.3,
    "HTML": 52.9,
    "Python": 51,
    "SQL": 51,
    "TypeScript": 38.5
}

# Step 2: Print dictionary / 打印字典
print("Programming Language Popularity Dictionary:")
print(lang_popularity)

# Step 3: Draw bar chart / 画柱状图
languages = list(lang_popularity.keys())  # 语言名称
percentages = list(lang_popularity.values())  # 使用百分比
plt.bar(languages, percentages, color='skyblue')  # 柱状图，颜色设为天蓝色
plt.title("Programming Language Popularity (Feb 2024)")  # 图标题
plt.xlabel("Languages")  # X轴标签
plt.ylabel("Percentage of Developers (%)")  # Y轴标签
plt.show()

# Step 4: Print percentage for a specific language / 打印某个语言的百分比
# Pseudocode: Define input language here / 伪代码：在这里定义输入语言
input_language = "Python"  # 可修改的变量，示例用 Python
percentage = lang_popularity[input_language]
print(f"Percentage of developers using {input_language}: {percentage}%")
'''
English: This code creates a dictionary, prints it, draws a bar chart, and prints the percentage for a chosen language (Python here).
中文：这段代码创建字典，打印出来，用 matplotlib 画柱状图，然后打印某个语言（这里是 Python）的百分比。
'''