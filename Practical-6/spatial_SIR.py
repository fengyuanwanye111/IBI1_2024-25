# spatial_SIR.py

# Pseudocode / 伪代码:
# BEGIN
#   Import numpy and matplotlib / 导入numpy和matplotlib
#   Create 100x100 array of susceptibles (0) / 创建100x100的易感人群数组(0)
#   Randomly infect one person (1) / 随机感染一个人(1)
#   Set beta=0.3 and gamma=0.05 / 设置beta=0.3和gamma=化妆品0.05
#   FOR t = 0 to 99:
#     FOR each infected person:
#       Check 8 neighbors / 检查8个邻居
#       Infect susceptible neighbors with prob beta / 以beta概率感染易感邻居
#       Recover with prob gamma / 以gamma概率康复
#     END FOR
#     Record population state / 记录人群状态
#   END FOR
#   Plot heatmaps at specific times / 在特定时间点绘制热图
# END

# 导入必要的库 / Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# 创建全易感人群数组 / Create array of all susceptible population
population = np.zeros((100, 100))  # 100x100数组，所有值为0 / 100x100 array, all values 0

# 随机选择一个感染起始点 / Randomly select one infection starting point
outbreak = np.random.choice(range(100), 2)  # 随机选择x,y坐标 / Randomly choose x,y coordinates
population[outbreak[0], outbreak[1]] = 1    # 将该点设为感染(1) / Set that point to infected(1)

# 定义模型参数 / Define model parameters
beta = 0.3   # 感染率 / Infection rate
gamma = 0.05 # 康复率 / Recovery rate

# 创建数组存储每个时间点状态 / Create array to store state at each time point
states = [population.copy()]  # 初始状态 / Initial state

# 时间循环 - 100个时间点 / Time loop - 100 time points
for t in range(100):
    # 获取当前感染者的位置 / Get locations of current infected
    infected = np.where(population == 1)  # 返回感染者的坐标 / Returns coordinates of infected
    new_pop = population.copy()  # 创建当前状态副本 / Create copy of current state
    
    # 对每个感染者处理 / Process each infected person
    for i in range(len(infected[0])):
        x, y = infected[0][i], infected[1][i]  # 获取感染者坐标 / Get infected coordinates
        
        # 检查8个邻居 / Check 8 neighbors
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:  # 跳过自身 / Skip self
                    continue
                nx, ny = x + dx, y + dy  # 新坐标 / New coordinates
                # 检查边界和状态 / Check bounds and state
                if (0 <= nx < 100 and 0 <= ny < 100 and new_pop[nx, ny] == 0):
                    # 以beta概率感染邻居 / Infect neighbor with probability beta
                    if np.random.random() < beta:
                        new_pop[nx, ny] = 1
    
    # 处理康复 / Process recoveries
    for i in range(len(infected[0])):
        x, y = infected[0][i], infected[1][i]  # 获取感染者坐标 / Get infected coordinates
        # 以gamma概率康复 / Recover with probability gamma
        if np.random.random() < gamma:
            new_pop[x, y] = 2  # 2表示康复 / 2 means recovered
    
    population = new_pop  # 更新人群状态 / Update population state
    states.append(population.copy())  # 记录当前状态 / Record current state

# 绘制特定时间点的热图 / Plot heatmaps at specific time points
time_points = [0, 10, 50, 100]  # 要显示的时间点 / Time points to display
plt.figure(figsize=(12, 8), dpi=150)  # 设置图形大小 / Set figure size

for i, t in enumerate(time_points):
    plt.subplot(2, 2, i+1)  # 创建2x2子图 / Create 2x2 subplot
    plt.imshow(states[t], cmap='viridis', interpolation='nearest')  # 绘制热图 / Plot heatmap
    plt.title(f'Time {t}')  # 设置标题 / Set title
    plt.axis('off')  # 关闭坐标轴 / Turn off axes

plt.tight_layout()  # 调整布局 / Adjust layout
plt.savefig('spatial_SIR.png')  # 保存图片 / Save figure
plt.show()  # 显示图形 / Show plot