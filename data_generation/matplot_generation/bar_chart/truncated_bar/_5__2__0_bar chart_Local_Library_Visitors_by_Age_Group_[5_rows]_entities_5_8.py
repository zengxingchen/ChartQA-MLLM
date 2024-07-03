
import matplotlib.pyplot as plt

# Data
countries = [
    "Luxembourg", "Switzerland", "Norway", "Ireland", "Qatar", 
    "United States", "Singapore", "Denmark", "Australia", "Sweden", 
    "Iceland", "Netherlands", "Austria", "Finland", "Germany", 
    "Belgium", "Canada", "United Kingdom", "France", "Japan"
]
gdp_per_capita = [
    115000, 87000, 83000, 82000, 81000, 65000, 62000, 61000, 
    60000, 58000, 57000, 56000, 55000, 53000, 52000, 51000, 
    50000, 49000, 47000, 46000
]

# Colors for each country
colors = [
    '#3498db', '#e74c3c', '#2ecc71', '#f1c40f', '#9b59b6', 
    '#34495e', '#e67e22', '#1abc9c', '#d35400', '#c0392b',
    '#2980b9', '#8e44ad', '#27ae60', '#d35400', '#8e44ad',
    '#3498db', '#2ecc71', '#e74c3c', '#34495e', '#f1c40f'
]

# Plot
fig, ax = plt.subplots(figsize=(15, 10)) # Adjusted size for horizontal layout
bars = ax.barh(countries, gdp_per_capita, color=colors, height=0.5) # Adjusted bar height to 0.5

# Set the title and labels
ax.set_title('Top 20 Countries by GDP per Capita', fontsize=15, pad=20)
ax.set_xlabel('GDP per Capita (USD)', fontsize=12)
ax.set_ylabel('Country', fontsize=12)

# Customize the tick labels
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

# Set the y-axis limit to start from 45000
ax.set_xlim(45000, 120000)

# Add the data values on the bars
for bar in bars:
    width = bar.get_width()
    label_x_pos = width + 2000
    ax.text(label_x_pos, bar.get_y() + bar.get_height()/2, f'{width} USD', va='center')

# Show the plot
plt.tight_layout()
plt.show()