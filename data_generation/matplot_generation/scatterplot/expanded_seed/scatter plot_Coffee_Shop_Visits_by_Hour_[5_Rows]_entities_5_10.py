
import matplotlib.pyplot as plt

# Data provided
data = [
    {'Hour': '08:00', 'Number of Visitors': 25},
    {'Hour': '10:00', 'Number of Visitors': 48},
    {'Hour': '13:00', 'Number of Visitors': 67},
    {'Hour': '15:00', 'Number of Visitors': 55},
    {'Hour': '18:00', 'Number of Visitors': 42}
]

# Extract Hours and Number of Visitors as separate lists
hours = [item['Hour'] for item in data]
number_of_visitors = [item['Number of Visitors'] for item in data]

# Convert 'Hour' from string to numerical value for plotting
# Assuming '08:00' is 8, '10:00' is 10, etc.
hour_values = [int(hour.split(':')[0]) for hour in hours]

# Create the scatter plot
plt.figure(figsize=(10, 5))  # Set the figure size
plt.scatter(hour_values, number_of_visitors, 
            s=[x*10 for x in number_of_visitors],  # Size corresponding to number of visitors
            c=range(len(hour_values)),  # Color based on time of day
            alpha=0.7,  # Transparency
            cmap='viridis',  # Color map
            edgecolors='w',  # Edge color of markers
            linewidth=2)  # Line width for edge colors

# Add labels for each point in the scatter plot
for i, txt in enumerate(number_of_visitors):
    plt.annotate(txt, (hour_values[i], number_of_visitors[i]), textcoords="offset points", xytext=(0,10), ha='center')

# Customize the axes
plt.xticks(hour_values, hours)  # Set x-axis ticks to be the hours
plt.ylim(0, max(number_of_visitors) + 20)  # Set y-axis limit to be slightly above the max visitors
plt.xlabel('Hour of the Day')  # x-axis label
plt.ylabel('Number of Visitors')  # y-axis label
plt.title('Number of Visitors by Hour')  # Title of the plot

# Show a colorbar and grid
plt.colorbar(label='Time of Day as Color')
plt.grid(True)

# Show the plot
plt.show()