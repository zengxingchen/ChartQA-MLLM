
import matplotlib.pyplot as plt

# Given data
data = [
    {'Age Group': '0-12', 'Number of Visitors': 150},
    {'Age Group': '13-18', 'Number of Visitors': 120},
    {'Age Group': '19-35', 'Number of Visitors': 200},
    {'Age Group': '36-50', 'Number of Visitors': 180},
    {'Age Group': '51+', 'Number of Visitors': 160}
]

# Extracting age groups and number of visitors from the table for plotting
age_groups = [item['Age Group'] for item in data]
visitors = [item['Number of Visitors'] for item in data]

# Creating a list of colors
colors = ['skyblue', 'orange', 'lightgreen', 'red', 'purple']

# Create the bar chart
plt.figure(figsize=(10, 6))  # Customize the size of the plot
bars = plt.bar(age_groups, visitors, color=colors)

# Add labels to the top of the bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 5, yval, ha='center', va='bottom')

# Add title and labels to the axes
plt.title('Number of Visitors by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Number of Visitors')

# Customize the grid
plt.grid(axis='y', linestyle='--', linewidth=0.7, alpha=0.7)

# Optional: Add a legend if you want to specify what colors mean in context
# plt.legend(['Age Groups'], loc='upper right')

# Displaying the plot
plt.show()