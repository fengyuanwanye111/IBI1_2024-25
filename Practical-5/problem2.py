# Pseudocode / 伪代码：
# 1. Create two lists for UK and China populations / 创建 UK 和中国人口的两个列表
# 2. Sort and print both lists / 排序并打印两个列表
# 3. Draw two pie charts with custom styles / 画两个自定义样式的饼图

import matplotlib.pyplot as plt

# Step 1: Create lists / 创建列表
uk_countries = [57.11, 3.13, 1.91, 5.45]  # England, Wales, N. Ireland, Scotland
zhejiang_neighbors = [65.77, 41.88, 45.28, 61.27, 85.15]  # Zhejiang, Fujian, Jiangxi, Anhui, Jiangsu
uk_labels = ["England", "Wales", "Northern Ireland", "Scotland"]
china_labels = ["Zhejiang", "Fujian", "Jiangxi", "Anhui", "Jiangsu"]

# Step 2: Sort and print lists / 排序并打印
uk_sorted = sorted(uk_countries)
china_sorted = sorted(zhejiang_neighbors)
print("Sorted UK Populations (millions):", uk_sorted)
print("Sorted Zhejiang Neighboring Provinces Populations (millions):", china_sorted)

# Step 3: Draw pie charts / 画饼图
# UK Pie Chart
plt.figure(1)  # 第一个图
plt.pie(uk_countries, labels=uk_labels, autopct='%1.1f%%', colors=['lightblue', 'lightgreen', 'lightcoral', 'lightyellow'], explode=(0.1, 0, 0, 0))
plt.title("UK Population Distribution (2022)")


# China Pie Chart
plt.figure(2)  # 第二个图
plt.pie(zhejiang_neighbors, labels=china_labels, autopct='%1.1f%%', colors=['salmon', 'gold', 'lightpink', 'cyan', 'lavender'], explode=(0, 0, 0, 0, 0.1))
plt.title("Zhejiang Neighboring Provinces Population Distribution (2022)")
plt.show()
'''
English: This code creates two lists, sorts and prints them, then draws two pie charts with custom colors and exploded slices.
中文：这段代码创建两个列表，排序并打印，然后画两个饼图，用自定义颜色和突出效果。
'''