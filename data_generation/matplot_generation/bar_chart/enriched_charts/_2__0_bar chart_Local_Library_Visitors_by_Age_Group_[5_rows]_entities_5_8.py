
import matplotlib.pyplot as plt

# Data
cities = [
    "New York", "Los Angeles", "Chicago", "Houston",
    "Phoenix", "Philadelphia", "San Antonio", "San Diego", 
    "Dallas", "San Jose", "Austin", "Jacksonville", "Fort Worth", 
    "Columbus", "Charlotte", "Seattle", "Denver", "Boston", 
    "Las Vegas", "Miami"
]
rainfall = [1250, 378, 988, 1496, 204, 1048, 831, 267, 940, 391, 859, 1120, 855, 961, 1162, 950, 370, 1165, 106, 1575]

# Colors for each city
colors = [
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
    '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
    '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf'
]

# Plot
fig, ax = plt.subplots(figsize=(10, 15)) # Adjusted size for vertical layout
bars = ax.bar(cities, rainfall, color=colors, width=0.7) # Adjusted bar width to 0.7

# Set the title and labels
ax.set_title('Average Annual Rainfall in Various Cities', fontsize=15, pad=20)
ax.set_xlabel('City', fontsize=12)
ax.set_ylabel('Average Annual Rainfall (mm)', fontsize=12)

# Customize the tick labels
plt.xticks(rotation=90, fontsize=10)
plt.yticks(fontsize=10)

# Add the data values on the bars
for bar in bars:
    height = bar.get_height()
    label_y_pos = height + 20
    ax.text(bar.get_x() + bar.get_width()/2, label_y_pos, f'{height} mm', ha='center')

# Show the plot
plt.tight_layout()
plt.show()