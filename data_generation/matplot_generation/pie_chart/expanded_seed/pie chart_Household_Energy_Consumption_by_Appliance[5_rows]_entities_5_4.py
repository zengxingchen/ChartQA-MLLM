
import matplotlib.pyplot as plt

# Given data
data = [
    {'Appliance': 'Refrigerator', 'Percentage': 30},
    {'Appliance': 'HVAC', 'Percentage': 25},
    {'Appliance': 'Water Heater', 'Percentage': 15},
    {'Appliance': 'Lighting', 'Percentage': 10},
    {'Appliance': 'Electronics', 'Percentage': 20}
]

# Preparing data for the pie chart
labels = [appliance['Appliance'] for appliance in data]
sizes = [appliance['Percentage'] for appliance in data]

# Define colors and explode (to highlight the 1st segment)
colors = ['skyblue', 'orange', 'lightgreen', 'yellow', 'lightcoral']
explode = (0.1, 0, 0, 0, 0)  # only "explode" the 1st slice (Refrigerator)

# Create a pie chart
plt.figure(figsize=(8, 8))
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)

# Add a title
plt.title('Energy Consumption by Appliance')

# Display the plot
plt.show()