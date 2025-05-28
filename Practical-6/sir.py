# SIR.py

# Pseudocode / 伪代码:
# BEGIN
#   Import numpy and matplotlib libraries / 导入numpy和matplotlib库
#   Set initial population values (N=10000, S=9999, I=1, R=0) / 设置初始人口值
#   Set beta=0.3 and gamma=0.05 / 设置beta=0.3和gamma=0.05
#   Create empty arrays for S, I, R / 创建S、I、R的空数组
#   FOR t = 0 to 999:
#     Calculate infection probability = beta * (I/N) / 计算感染概率
#     Choose new infections randomly from S / 从S中随机选择新感染者
#     Choose new recoveries randomly from I / 从I中随机选择新康复者
#     Update S, I, R values / 更新S、I、R值
#     Append values to arrays / 将值添加到数组
#   END FOR
#   Plot S, I, R curves / 绘制S、I、R曲线
#   Save figure / 保存图片
# END

# 导入必要的库 / Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# 定义初始变量 / Define initial variables
N = 10000  # 总人口 / Total population
S = 9999   # 易感人群 / Susceptible population
I = 1      # 感染人群 / Infected population
R = 0      # 康复人群 / Recovered population
beta = 0.3   # 感染率 / Infection rate
gamma = 0.05 # 康复率 / Recovery rate

# 创建数组来跟踪变量随时间的变化 / Create arrays to track variables over time
susceptible = [S]  # 易感人群数组 / Susceptible array
infected = [I]     # 感染人群数组 / Infected array
recovered = [R]    # 康复人群数组 / Recovered array

# 时间循环 - 1000个时间点 / Time loop - 1000 time points
for t in range(1000):
    # 计算每个易感个体的感染概率 / Calculate infection probability for each susceptible
    infection_prob = beta * (I/N)
    
    # 添加保护机制防止负值 / Add protection against negative values
    new_infections = min(S, np.random.choice([0, 1], size=S, p=[1-infection_prob, infection_prob]).sum())
    new_recoveries = min(I, np.random.choice([0, 1], size=I, p=[1-gamma, gamma]).sum())
    
    # 更新人口数值 / Update population values
    S = S - new_infections          # 易感人群减少 / Susceptible decreases
    I = I + new_infections - new_recoveries  # 感染人群变化 / Infected changes
    R = R + new_recoveries          # 康复人群增加 / Recovered increases
    
    # 确保数值不变成负数 / Ensure values don't go negative
    S = max(0, S)
    I = max(0, I)
    R = max(0, R)
    
    # 记录每个时间步的结果 / Record values for each time step
    susceptible.append(S)  # 添加易感人数 / Add susceptible count
    infected.append(I)     # 添加感染人数 / Add infected count
    recovered.append(R)    # 添加康复人数 / Add recovered count

# 创建图形 / Create the plot
plt.figure(figsize=(6, 4), dpi=150)  # 设置图形大小和分辨率 / Set figure size and resolution
plt.plot(susceptible, label='Susceptible')  # 绘制易感曲线 / Plot susceptible curve
plt.plot(infected, label='Infected')       # 绘制感染曲线 / Plot infected curve
plt.plot(recovered, label='Recovered')     # 绘制康复曲线 / Plot recovered curve
plt.xlabel('Time')                         # X轴标签 / X-axis label
plt.ylabel('Number of People')             # Y轴标签 / Y-axis label
plt.title('SIR Model Simulation')   # 图标题 / Plot title
plt.legend()                                   # 添加图例 / Add legend
plt.grid(True)                                 # 添加网格 / Add grid
plt.savefig('SIR_plot.png')                    # 保存图片 / Save figure (移除type参数)
plt.show()                                     # 显示图形 / Show plot

# 基本验证 / Basic verification
print(f"Final S: {S}")              # 打印最终易感人数 / Print final susceptible
print(f"Final I: {I}")              # 打印最终感染人数 / Print final infected
print(f"Final R: {R}")              # 打印最终康复人数 / Print final recovered
print(f"Total population check: {S + I + R} (should equal {N})")  # 验证总人口 / Verify total population