
import matplotlib.pyplot as plt

# Data
years = ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023']
research_spending = [22.5, 23.8, 25.0, 27.1, 29.3, 31.6, 34.0, 36.5, 39.1]

# Create vertical bar chart
fig, ax = plt.subplots(figsize=(10, 14))

bars = ax.bar(years, research_spending, width=0.5, color=['#1E90FF', '#32CD32', '#FFD700', '#FF4500', '#8A2BE2', '#FF69B4', '#A52A2A', '#5F9EA0', '#D2691E'])

# Customizing the plot
ax.set_title('Annual Research Spending (2015-2023)', fontsize=20, pad=20)
ax.set_ylabel('Research Spending (in billion USD)', fontsize=16)
ax.set_xlabel('Year', fontsize=16)

# Set bar labels to show the spending values
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, height, f'{height} bn', ha='center', va='bottom')

# Set y-axis limits to truncate the chart and start from a specific value
ax.set_ylim(20, 45)

# Show the plot
plt.tight_layout()
plt.show()