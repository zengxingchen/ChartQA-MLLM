
import matplotlib.pyplot as plt

# Data for plotting
countries = ['Australia', 'Canada', 'France', 'Germany', 'Italy', 'Japan', 'Netherlands', 'Spain', 'Sweden', 'UK']
expenditure = [129, 145, 167, 211, 214, 225, 276, 332, 390, 440]

# Define the colors for each bar
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#A633FF', '#FF8C33', '#33FFD6', '#D633FF', '#FFBD33', '#33FFBD']

fig, ax = plt.subplots(figsize=(10, 14))

# Create vertical bars
ax.bar(countries, expenditure, color=colors, edgecolor='black', width=0.6)

# Set chart title and labels
ax.set_title('Research & Development Expenditure by Country (2024)', fontsize=18, pad=20)
ax.set_ylabel('Expenditure (Billions USD)', fontsize=14)
ax.set_xlabel('Country', fontsize=14)

# Set the limits for the y-axis
ax.set_ylim(100, max(expenditure) + 50)

# Show the actual data points on the bars
for i, v in enumerate(expenditure):
    ax.text(i, v + 10, str(v), color='black', ha='center', fontsize=12)

# Removing the spines
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

# Turn off x ticks for cleaner look
ax.xaxis.set_ticks_position('none')

# Show grid
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Show the plot
plt.show()