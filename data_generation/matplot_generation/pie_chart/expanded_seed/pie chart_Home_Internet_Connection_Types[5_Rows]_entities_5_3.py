
import matplotlib.pyplot as plt

# Data from the chart table provided by the user
data = [
    {'Type': 'Fiber', 'Percentage of Households': 21},
    {'Type': 'Cable', 'Percentage of Households': 54},
    {'Type': 'DSL', 'Percentage of Households': 16},
    {'Type': 'Satellite', 'Percentage of Households': 3},
    {'Type': 'Fixed Wireless', 'Percentage of Households': 6}
]

# Extracting the 'Type' and 'Percentage of Households' for plotting
types = [entry['Type'] for entry in data]
percentages = [entry['Percentage of Households'] for entry in data]

# Define colors for each slice
colors = ['gold', 'lightskyblue', 'lightcoral', 'lightgreen', 'orange']

# Explode the largest piece (Cable) to highlight it
explode = [0.1 if entry['Type'] == 'Cable' else 0 for entry in data]

# Create a pie chart
plt.figure(figsize=(8, 8)) # Set the figure size
plt.pie(percentages, labels=types, autopct='%1.1f%%', startangle=140, colors=colors, explode=explode, shadow=True)

# Add a title to the pie chart
plt.title('Percentage of Households by Internet Connection Type')

# Draw a circle at the center to turn the pie into a donut chart
centre_circle = plt.Circle((0,0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle.
plt.axis('equal')

# Display the pie chart
plt.show()