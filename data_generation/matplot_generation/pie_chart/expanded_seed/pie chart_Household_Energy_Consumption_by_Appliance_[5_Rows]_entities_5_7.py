
import matplotlib.pyplot as plt

# Given data
data = [
    {'Appliance': 'Refrigerator', 'Energy Consumption (kWh)': 600},
    {'Appliance': 'HVAC System', 'Energy Consumption (kWh)': 350},
    {'Appliance': 'Washing Machine', 'Energy Consumption (kWh)': 250},
    {'Appliance': 'Lighting', 'Energy Consumption (kWh)': 150},
    {'Appliance': 'Television', 'Energy Consumption (kWh)': 50}
]

# Extracting appliance names and energy consumption values
appliances = [item['Appliance'] for item in data]
energy_consumption = [item['Energy Consumption (kWh)'] for item in data]

# Defining colors for each pie slice
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99', '#c2c2f0']

# To highlight certain slices, the 'explode' parameter can be adjusted
explode = (0.1, 0, 0, 0, 0)  # only "explode" the 1st slice (Refrigerator)

# Create a pie chart
plt.figure(figsize=(10, 7))
plt.pie(energy_consumption, labels=appliances, autopct='%1.1f%%', startangle=140, colors=colors, explode=explode, shadow=True)

# Draw a circle at the center of pie to make it look like a donut
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle
plt.axis('equal')  

# Adding a title
plt.title('Energy Consumption by Appliance')

# Show the plot
plt.show()