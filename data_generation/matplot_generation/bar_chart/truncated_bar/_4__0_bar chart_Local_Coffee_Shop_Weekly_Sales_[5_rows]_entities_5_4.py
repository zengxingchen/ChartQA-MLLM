
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
average_rainfall = [110, 115, 130, 145, 160, 170, 180, 200, 190, 175, 150, 140]

# Color scheme using specific color codes
colors = ['#0072B2', '#56B4E9', '#009E73', '#F0E442', '#E69F00', '#D55E00',
          '#CC79A7', '#999999', '#66C2A5', '#FC8D62', '#8DA0CB', '#E78AC3']

# Create vertical bar chart
plt.figure(figsize=(12, 10))
bars = plt.bar(months, average_rainfall, color=colors, width=0.6)

# Adjusting the height of bars by setting the y-axis limits
plt.ylim(100, max(average_rainfall) + 20)  # Truncated y-axis starting from 100

# Changing the layout and labels
plt.ylabel('Average Monthly Rainfall (mm)', fontsize=12)
plt.title('Average Monthly Rainfall in a Year', fontsize=16)
plt.xticks(rotation=45, ha='right')

# Adding value labels above each bar
for i, v in enumerate(average_rainfall):
    plt.text(i, v + 2, str(v), color='black', ha='center', fontsize=11)

# Show the final result
plt.tight_layout()
plt.show()