# SIR_vaccination.py

# Pseudocode / 伪代码:
# BEGIN
#   Import numpy, matplotlib and cm libraries / 导入numpy、matplotlib和cm库
#   Set initial population (N=10000) and vaccination rates / 设置初始人口和疫苗接种率
#   FOR each vaccination percentage:
#     Set S, I, R, V (vaccinated) initial values / 设置S、I、R、V初始值
#     Create arrays for S, I, R, V / 创建S、I、R、V数组
#     FOR t = 0 to 999:
#       Calculate infection probability / 计算感染概率
#       Update S, I, R (V remains constant) / 更新S、I、R (V保持不变)
#       Record values / 记录数值
#     END FOR
#     Plot infected curve / 绘制感染曲线
#   END FOR
#   Show plot with legend / 显示带图例的图表
# END

# 导入必要的库 / Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm  # 导入颜色映射 / Import color map

# 定义基本参数 / Define basic parameters
N = 10000  # 总人口 / Total population
beta = 0.3   # 感染率 / Infection rate
gamma = 0.05 # 康复率 / Recovery rate
vacc_rates = [0, 0.1, 0.3, 0.5, 0.7, 0.9]  # 不同疫苗接种率 / Different vaccination rates

# 创建图形 / Create figure
plt.figure(figsize=(8, 6), dpi=150)  # 设置图形大小和分辨率 / Set figure size and resolution

# 对每种疫苗接种率进行模拟 / Simulate for each vaccination rate
for idx, vacc_rate in enumerate(vacc_rates):
    # 初始化人群 / Initialize populations
    V = int(N * vacc_rate)    # 接种疫苗人数 / Vaccinated population
    S = N - V - 1            # 易感人群 / Susceptible (total - vaccinated - 1 initial infected)
    I = 1                    # 感染人群 / Infected
    R = 0                    # 康复人群 / Recovered
    
    # 创建数组 / Create arrays
    susceptible = [S]  # 易感人群数组 / Susceptible array
    infected = [I]     # 感染人群数组 / Infected array
    recovered = [R]    # 康复人群数组 / Recovered array
    
    # 时间循环 / Time loop
    for t in range(1000):
        # 计算感染概率 / Calculate infection probability
        infection_prob = beta * (I/(N-V))  # 注意：只考虑未接种人群 / Note: only unvaccinated population
        
        # 更新人数 / Update numbers
        new_infections = min(S, np.random.choice([0, 1], size=S, p=[1-infection_prob, infection_prob]).sum())
        new_recoveries = min(I, np.random.choice([0, 1], size=I, p=[1-gamma, gamma]).sum())
        
        S = max(0, S - new_infections)          # 更新易感人数 / Update susceptible
        I = max(0, I + new_infections - new_recoveries)  # 更新感染人数 / Update infected
        R = max(0, R + new_recoveries)          # 更新康复人数 / Update recovered
        
        # 记录数据 / Record data
        susceptible.append(S)
        infected.append(I)
        recovered.append(R)
    
    # 绘制感染曲线，使用viridis颜色 / Plot infected curve with viridis colormap
    plt.plot(infected, label=f'Vacc Rate {vacc_rate*100}%', 
             color=cm.viridis(idx * 40))  # 使用不同颜色 / Use different colors

# 设置图形属性 / Set plot properties
plt.xlabel('时间/Time')                          # X轴标签 / X-axis label
plt.ylabel('感染人数/Number of Infected')        # Y轴标签 / Y-axis label
plt.title('不同接种率下的感染人数/SIR Model with Vaccination')  # 图标题 / Plot title
plt.legend()                                    # 添加图例 / Add legend
plt.grid(True)                                  # 添加网格 / Add grid
plt.savefig('SIR_vaccination.png')              # 保存图片 / Save figure
plt.show()                                      # 显示图形 / Show plot