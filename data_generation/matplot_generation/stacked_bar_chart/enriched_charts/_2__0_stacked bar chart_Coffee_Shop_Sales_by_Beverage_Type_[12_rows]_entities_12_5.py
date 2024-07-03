
import matplotlib.pyplot as plt

# Data
years = ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025']
population_growth = [1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800, 3000]
immigration = [200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700]
emigration = [100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600]
birth_rate = [500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500]
death_rate = [300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800]

# Plot
fig, ax = plt.subplots(figsize=(12, 10))  # Change width and height of the chart

bar_width = 0.6

ax.bar(years, population_growth, color='#ff9999', edgecolor='white', width=bar_width, label='Population Growth')
ax.bar(years, immigration, bottom=population_growth, color='#66b3ff', edgecolor='white', width=bar_width, label='Immigration')
ax.bar(years, emigration, bottom=[i+j for i,j in zip(population_growth, immigration)], color='#99ff99', edgecolor='white', width=bar_width, label='Emigration')
ax.bar(years, birth_rate, bottom=[i+j+k for i,j,k in zip(population_growth, immigration, emigration)], color='#ffcc99', edgecolor='white', width=bar_width, label='Birth Rate')
ax.bar(years, death_rate, bottom=[i+j+k+l for i,j,k,l in zip(population_growth, immigration, emigration, birth_rate)], color='#c2c2f0', edgecolor='white', width=bar_width, label='Death Rate')

ax.set_ylabel('Number of People')
ax.set_title('Population Dynamics from 2015 to 2025')
ax.set_xticks(years)
ax.set_ylim(0, 10000)  # Adjust to accommodate the sum of the data points
ax.legend(loc='upper left')

# Adding numerical labels to each bar
for i in range(len(years)):
    plt.text(i, population_growth[i]/2, str(population_growth[i]), ha='center', va='center', color='black', fontweight='bold')
    plt.text(i, population_growth[i] + immigration[i]/2, str(immigration[i]), ha='center', va='center', color='black', fontweight='bold')
    plt.text(i, population_growth[i] + immigration[i] + emigration[i]/2, str(emigration[i]), ha='center', va='center', color='black', fontweight='bold')
    plt.text(i, population_growth[i] + immigration[i] + emigration[i] + birth_rate[i]/2, str(birth_rate[i]), ha='center', va='center', color='black', fontweight='bold')
    plt.text(i, population_growth[i] + immigration[i] + emigration[i] + birth_rate[i] + death_rate[i]/2, str(death_rate[i]), ha='center', va='center', color='black', fontweight='bold')

plt.show()