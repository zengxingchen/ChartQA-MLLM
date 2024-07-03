
import matplotlib.pyplot as plt

# Data for stacked area chart
years = range(2012, 2023)
ai_research = [2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000]
quantum_computing = [1500, 1700, 1900, 2100, 2300, 2500, 2700, 2900, 3100, 3300, 3500]
biotechnology = [1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800, 3000, 3200]
robotics = [800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800]

# Plot
plt.figure(figsize=(16, 10))  # Change width and height of the chart
plt.stackplot(years, ai_research, quantum_computing, biotechnology, robotics, 
              colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'])

# Customize the plot
plt.title('Advancements in Future Technologies from 2012 to 2022', fontsize=18, pad=30)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Number of Publications', fontsize=14)
plt.legend(['AI Research', 'Quantum Computing', 'Biotechnology', 'Robotics'], loc='upper left')

# Annotation
for i, y in enumerate(years):
    plt.annotate(f'{ai_research[i]}', (y, ai_research[i]), textcoords="offset points", xytext=(0,5), ha='center', fontsize=8)
    plt.annotate(f'{quantum_computing[i]}', (y, ai_research[i] + quantum_computing[i]), textcoords="offset points", xytext=(0,5), ha='center', fontsize=8)
    plt.annotate(f'{biotechnology[i]}', (y, ai_research[i] + quantum_computing[i] + biotechnology[i]), textcoords="offset points", xytext=(0,5), ha='center', fontsize=8)
    plt.annotate(f'{robotics[i]}', (y, ai_research[i] + quantum_computing[i] + biotechnology[i] + robotics[i]), textcoords="offset points", xytext=(0,5), ha='center', fontsize=8)

plt.show()