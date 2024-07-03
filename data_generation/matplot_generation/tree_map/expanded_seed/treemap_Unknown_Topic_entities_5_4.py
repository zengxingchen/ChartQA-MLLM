
import matplotlib.pyplot as plt
import squarify  # you might need to install squarify with pip install squarify

# Given table data
data = [
    {'Day': 'Monday', 'Breakfast Item': 'Cereal', 'Calories Consumed': 150, 'Percentage of Adults Consuming': '35%'},
    {'Day': 'Tuesday', 'Breakfast Item': 'Eggs and Toast', 'Calories Consumed': 350, 'Percentage of Adults Consuming': '40%'},
    {'Day': 'Wednesday', 'Breakfast Item': 'Oatmeal', 'Calories Consumed': 200, 'Percentage of Adults Consuming': '25%'},
    {'Day': 'Thursday', 'Breakfast Item': 'Smoothie', 'Calories Consumed': 250, 'Percentage of Adults Consuming': '15%'},
    {'Day': 'Friday', 'Breakfast Item': 'Bagel with Cream Cheese', 'Calories Consumed': 450, 'Percentage of Adults Consuming': '20%'}
]

# Extract the necessary information for the plot
labels = ['{} - {} - {} - {} cal'.format(d['Day'], d['Breakfast Item'], d['Percentage of Adults Consuming'], d['Calories Consumed']) for d in data]
sizes = [d['Calories Consumed'] for d in data]
colors = plt.cm.Paired(range(len(sizes)))  # generate a color for each different size

# Create the treemap
squarify.plot(sizes=sizes, label=labels, color=colors, alpha=0.7)

# Configure plot
plt.title('Breakfast Item Popularity and Caloric Content', fontsize=15)
plt.axis('off')  # Disable the axes

# Show the plot
plt.show()