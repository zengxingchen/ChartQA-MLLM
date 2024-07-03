
import matplotlib.pyplot as plt

# Data
countries = ['USA', 'Canada', 'Germany', 'UK', 'Australia', 'India', 'China', 'Japan', 'Brazil', 'South Africa']
early_childhood = [2000, 1800, 1600, 1700, 1500, 1400, 1300, 1200, 1100, 1000]
primary = [15000, 14000, 13500, 14500, 13800, 11000, 10500, 10800, 10000, 9800]
secondary = [13000, 12500, 12000, 12750, 11800, 9500, 9000, 9200, 8500, 8000]
higher_education = [9000, 8500, 8000, 8750, 7800, 6500, 6000, 6200, 5800, 5600]

# Colors for each education level
colors = ['#4c72b0', '#55a868', '#c44e52', '#8172b2']

# Figure size
plt.figure(figsize=(12, 6))

# Bar widths (change to height for horizontal bars)
bar_width = 0.6

# Plotting
plt.bar(countries, early_childhood, color=colors[0], edgecolor='white', width=bar_width, label='Early Childhood')
plt.bar(countries, primary, bottom=early_childhood, color=colors[1], edgecolor='white', width=bar_width, label='Primary')
plt.bar(countries, [early_childhood[i] + primary[i] for i in range(len(secondary))], bottom=[primary[i] for i in range(len(secondary))], color=colors[2], edgecolor='white', width=bar_width, label='Secondary')
plt.bar(countries, [early_childhood[i] + primary[i] + secondary[i] for i in range(len(higher_education))], bottom=[early_childhood[i] + primary[i] for i in range(len(secondary))], color=colors[3], edgecolor='white', width=bar_width, label='Higher Education')

# Labels and Title
plt.ylabel('Number of Students')
plt.title('Number of Students Enrolled by Education Level and Country')
plt.legend()

# Numerical labels for each bar segment
for i in range(len(countries)):
    plt.text(i, early_childhood[i] / 2, str(early_childhood[i]), ha='center', va='center', color='white')
    plt.text(i, early_childhood[i] + primary[i] / 2, str(primary[i]), ha='center', va='center', color='white')
    plt.text(i, early_childhood[i] + primary[i] + secondary[i] / 2, str(secondary[i]), ha='center', va='center', color='white')
    plt.text(i, early_childhood[i] + primary[i] + secondary[i] + higher_education[i] / 2, str(higher_education[i]), ha='center', va='center', color='white')

# Display the plot
plt.tight_layout()
plt.show()