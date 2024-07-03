
import matplotlib.pyplot as plt

# Data provided
data = [
    {'Appliance': 'Refrigerator', 'Percentage of Energy Use': '30%'},
    {'Appliance': 'HVAC System', 'Percentage of Energy Use': '25%'},
    {'Appliance': 'Water Heater', 'Percentage of Energy Use': '20%'},
    {'Appliance': 'Washer and Dryer', 'Percentage of Energy Use': '15%'},
    {'Appliance': 'Lighting', 'Percentage of Energy Use': '10%'}
]

# Extract appliance names and energy percentages
appliances = [item['Appliance'] for item in data]
percentages = [int(item['Percentage of Energy Use'].rstrip('%')) for item in data]

# Colors for the pie chart
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0']

# Explode the 1st slice (Refrigerator)
explode = (0.1, 0, 0, 0, 0)  # only "explode" the 1st slice

# Plotting the pie chart
plt.figure(figsize=(8, 8))
plt.pie(percentages, labels=appliances, colors=colors, explode=explode,
        autopct='%1.1f%%', shadow=True, startangle=140)

plt.title('Energy Use by Appliance')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Display the pie chart
plt.show()