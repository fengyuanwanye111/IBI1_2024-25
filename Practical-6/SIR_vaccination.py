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

# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm # For colormaps

# Define basic model parameters
N = 10000          # Total population
beta = 0.3         # Infection rate (probability of infection given contact with an infected individual)
gamma = 0.05       # Recovery rate (probability of an infected individual recovering)
time_steps = 1000  # Number of time steps to simulate

# List of different vaccination rates (percentages) to simulate
vacc_rates = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

# Initialize the plot
plt.figure(figsize=(10, 7), dpi=150) # Set figure size and resolution

# Loop through each vaccination rate
for idx, vacc_rate in enumerate(vacc_rates):
    # Initialize populations for the current simulation
    V = int(N * vacc_rate)  # Number of vaccinated individuals

    if vacc_rate == 1.0:
        # If 100% vaccination, assume no susceptible and thus no initial infected among non-vaccinated
        S = 0
        I = 0
        R = 0
    else:
        # Start with one infected individual among the non-vaccinated
        I = 1
        # Susceptible individuals are those not vaccinated and not initially infected
        S = N - V - I
        R = 0
        # Ensure S is not negative due to V + I potentially exceeding N (edge case with small N)
        S = max(0, S)


    # Lists to store the state of S, I, R over time for plotting
    susceptible_over_time = [S]
    infected_over_time = [I]
    recovered_over_time = [R]

    # Simulate the epidemic over time_steps
    for t in range(time_steps):
        infection_prob = 0.0 # Default infection probability
        # Calculate infection probability only if there are susceptible, infected, and unvaccinated individuals
        if S > 0 and I > 0 and (N - V) > 0:
            # Proportion of infected among the non-vaccinated population
            proportion_infected_among_non_vaccinated = I / (N - V)
            infection_prob = beta * proportion_infected_among_non_vaccinated

        new_infections = 0
        if S > 0 and infection_prob > 0:
            # Each susceptible individual has a 'infection_prob' chance of getting infected
            # We use np.random.choice to simulate this for all S individuals
            # The sum gives the total number of new infections in this time step
            infected_outcomes = np.random.choice([0, 1], size=S, p=[1 - infection_prob, infection_prob])
            new_infections = infected_outcomes.sum()

        new_recoveries = 0
        if I > 0:
            # Each infected individual has a 'gamma' chance of recovering
            recovered_outcomes = np.random.choice([0, 1], size=I, p=[1 - gamma, gamma])
            new_recoveries = recovered_outcomes.sum()

        # Update the S, I, R counts for the next time step
        S_next = S - new_infections
        I_next = I + new_infections - new_recoveries
        R_next = R + new_recoveries # R only increases or stays same as people don't lose immunity

        # Ensure populations are not negative (as a safeguard, though the logic above should prevent it)
        S = max(0, S_next)
        I = max(0, I_next)
        R = R_next # R is cumulative

        # Store the current counts
        susceptible_over_time.append(S)
        infected_over_time.append(I)
        recovered_over_time.append(R)

    # Plot the number of infected people over time for the current vaccination rate
    # Use a color from the 'viridis' colormap, varying by index
    if len(vacc_rates) > 1:
        color_value = idx / (len(vacc_rates) - 1)
    else:
        color_value = 0.5 # Default color if only one rate is plotted
    plt.plot(infected_over_time, label=f'{vacc_rate*100:.0f}% Vaccinated', color=cm.viridis(color_value))

# Configure the plot details
plt.xlabel('Time Steps')
plt.ylabel('Number of Infected Individuals')
plt.title('SIR Model: Impact of Vaccination Rates on Infections')
plt.legend(title="Vaccination Rate", bbox_to_anchor=(1.05, 1), loc='upper left') # Place legend outside plot
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout(rect=[0, 0, 0.85, 1]) # Adjust layout to make space for legend outside

# Save the figure
plt.savefig('SIR_vaccination_impact.png')

# Show the plot
plt.show()