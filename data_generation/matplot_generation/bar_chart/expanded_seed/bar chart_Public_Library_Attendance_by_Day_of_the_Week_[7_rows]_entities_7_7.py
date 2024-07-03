
import matplotlib.pyplot as plt

# Dataset
data = [
    {'Day': 'Monday', 'Visitors': 120},
    {'Day': 'Tuesday', 'Visitors': 135},
    {'Day': 'Wednesday', 'Visitors': 150},
    {'Day': 'Thursday', 'Visitors': 160},
    {'Day': 'Friday', 'Visitors': 175},
    {'Day': 'Saturday', 'Visitors': 200},
    {'Day': 'Sunday', 'Visitors': 80}
]

# Extracting days and visitors for plotting
days = [day['Day'] for day in data]
visitors = [day['Visitors'] for day in data]

# Colors for the bars
colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#F0E68C', '#FF6666', '#ADD8E6']

# Create the bar chart
plt.figure(figsize=(10, 6))  # Set the size of the figure (width, height)
bars = plt.bar(days, visitors, color=colors, edgecolor='black')

# Add a title
plt.title('Visitors per Day')

# Add labels to the axes
plt.xlabel('Day of the Week')
plt.ylabel('Number of Visitors')

# Customize the tick labels on the x-axis
plt.xticks(rotation=45, ha='right')

# Adding value labels on top of each bar
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 5, yval, ha='center', va='bottom')

# Optional: Add a grid
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show the plot
plt.show()