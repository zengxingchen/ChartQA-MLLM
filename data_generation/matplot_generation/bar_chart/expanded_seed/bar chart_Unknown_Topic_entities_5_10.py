
import matplotlib.pyplot as plt

# The provided data
data = [
    {'Day of the Week': 'Monday', 'Minutes of Exercise': 30},
    {'Day of the Week': 'Tuesday', 'Minutes of Exercise': 45},
    {'Day of the Week': 'Wednesday', 'Minutes of Exercise': 60},
    {'Day of the Week': 'Thursday', 'Minutes of Exercise': 20},
    {'Day of the Week': 'Friday', 'Minutes of Exercise': 50}
]

# Extracting the days and the minutes from the data
days = [item['Day of the Week'] for item in data]
minutes = [item['Minutes of Exercise'] for item in data]

# Setting up the colors for each bar to make the chart more colorful
colors = ['blue', 'green', 'red', 'cyan', 'magenta']

# Creating the bar chart
plt.figure(figsize=(10, 6))  # Larger figure size for better readability
bars = plt.bar(days, minutes, color=colors, edgecolor='black')  # Colorful bars with black edges

# Adding value labels on top of each bar
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 2, int(yval), ha='center', va='bottom')

# Adding the title and labels
plt.title('Minutes of Exercise Per Day of the Week', fontsize=16)  # Title of the chart
plt.xlabel('Day of the Week', fontsize=12)  # X-axis label
plt.ylabel('Minutes of Exercise', fontsize=12)  # Y-axis label

# Adding a grid to the y-axis to improve readability of the value for each bar
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Optional: Rotate the x-axis labels if they are too long and overlap
plt.xticks(rotation=45)

# Display the created plot
plt.show()