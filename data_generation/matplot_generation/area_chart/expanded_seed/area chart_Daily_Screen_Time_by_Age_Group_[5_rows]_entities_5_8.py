
import matplotlib.pyplot as plt

# Data from the chart table provided
data = [
    {'Age Group': '0-10', ' Average Daily Screen Time (hours)': 1.5},
    {'Age Group': '11-20', ' Average Daily Screen Time (hours)': 4.0},
    {'Age Group': '21-35', ' Average Daily Screen Time (hours)': 5.5},
    {'Age Group': '36-50', ' Average Daily Screen Time (hours)': 4.5},
    {'Age Group': '51+', ' Average Daily Screen Time (hours)': 3.0}
]

# Extract the age groups and screen times into lists
age_groups = [item['Age Group'] for item in data]
screen_times = [item[' Average Daily Screen Time (hours)'] for item in data]

# Create the x points for the area chart, which correspond to the age groups
x_range = range(len(age_groups))

# Start the area chart with the lowest level (zero line)
plt.fill_between(x_range, 0, screen_times[0], color='skyblue', alpha=0.5)

# Plot each segment of the area chart and stack them correctly
for i in range(1, len(screen_times)):
    plt.fill_between(x_range, screen_times[i-1], screen_times[i],
                     color='skyblue', alpha=(i + 1) * 0.1)

# Add some visual enhancements
plt.xticks(x_range, age_groups)  # Set the x-axis to show the age group labels
plt.xlabel('Age Group')  # X-axis label
plt.ylabel('Average Daily Screen Time (hours)')  # Y-axis label
plt.title('Average Daily Screen Time by Age Group')  # Chart title

# Add a grid to make the chart easier to read
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Show the plot
plt.show()