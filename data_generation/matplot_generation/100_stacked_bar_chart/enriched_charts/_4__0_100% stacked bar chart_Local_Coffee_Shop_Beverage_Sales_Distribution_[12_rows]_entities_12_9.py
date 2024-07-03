
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
health = [18, 20, 15, 25, 20, 20, 15, 23, 10, 30, 20, 18]
technology = [22, 18, 25, 10, 15, 18, 22, 25, 25, 10, 15, 20]
education = [25, 20, 15, 30, 20, 20, 25, 20, 15, 30, 20, 28]
environment = [15, 25, 20, 15, 25, 20, 15, 22, 25, 20, 25, 12]
entertainment = [10, 15, 10, 10, 20, 10, 18, 12, 15, 10, 20, 10]
travel = [10, 12, 15, 10, 15, 12, 15, 10, 10, 15, 10, 15]

bar_width = 0.8

fig, ax = plt.subplots(figsize=(10, 12))

# Bottom values for stacking
bar_technology = list(health)
bar_education = [i + j for i, j in zip(bar_technology, technology)]
bar_environment = [i + j for i, j in zip(bar_education, education)]
bar_entertainment = [i + j for i, j in zip(bar_environment, environment)]
bar_travel = [i + j for i, j in zip(bar_entertainment, entertainment)]

# Stacked bars
plt.bar(months, health, color='#1f77b4', edgecolor='white', width=bar_width)
plt.bar(months, technology, bottom=bar_technology, color='#ff7f0e', edgecolor='white', width=bar_width)
plt.bar(months, education, bottom=bar_education, color='#2ca02c', edgecolor='white', width=bar_width)
plt.bar(months, environment, bottom=bar_environment, color='#d62728', edgecolor='white', width=bar_width)
plt.bar(months, entertainment, bottom=bar_entertainment, color='#9467bd', edgecolor='white', width=bar_width)
plt.bar(months, travel, bottom=bar_travel, color='#8c564b', edgecolor='white', width=bar_width)

# Labels
plt.ylabel('Percentage (%)')
plt.title('Monthly Activity Distribution Across Different Categories')
plt.xticks(rotation=45, ha='right')
plt.yticks(range(0, 101, 10))

# Show percentages on the bars
for i in range(len(months)):
    plt.text(i, health[i] / 2, str(health[i]) + '%', ha='center', va='center', color='white', fontsize=8)
    plt.text(i, bar_technology[i] + technology[i] / 2, str(technology[i]) + '%', ha='center', va='center', color='white', fontsize=8)
    plt.text(i, bar_education[i] + education[i] / 2, str(education[i]) + '%', ha='center', va='center', color='white', fontsize=8)
    plt.text(i, bar_environment[i] + environment[i] / 2, str(environment[i]) + '%', ha='center', va='center', color='white', fontsize=8)
    plt.text(i, bar_entertainment[i] + entertainment[i] / 2, str(entertainment[i]) + '%', ha='center', va='center', color='white', fontsize=8)
    plt.text(i, bar_travel[i] + travel[i] / 2, str(travel[i]) + '%', ha='center', va='center', color='white', fontsize=8)

# Show the plot
plt.show()