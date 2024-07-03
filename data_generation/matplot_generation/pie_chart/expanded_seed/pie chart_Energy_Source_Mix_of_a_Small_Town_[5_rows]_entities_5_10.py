
import matplotlib.pyplot as plt

# Given chart data
data = [
    {'Energy Source': 'Solar', 'Percentage': 25},
    {'Energy Source': 'Wind', 'Percentage': 15},
    {'Energy Source': 'Hydropower', 'Percentage': 30},
    {'Energy Source': 'Natural Gas', 'Percentage': 20},
    {'Energy Source': 'Nuclear', 'Percentage': 10}
]

# Extracting the 'Energy Source' names and 'Percentage' values
labels = [item['Energy Source'] for item in data]
sizes = [item['Percentage'] for item in data]

# Define colors for each energy source
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0']

# Explode the 1st slice (Solar)
explode = (0.1, 0, 0, 0, 0)  

# Plotting the pie chart
fig1, ax1 = plt.subplots()

# Automatically format the percentage value and add a percentage sign at the end
ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)

# Equal aspect ratio ensures that pie is drawn as a circle (maintain the circular shape)
ax1.axis('equal')  

# Title of the pie chart
plt.title('Energy Source Distribution')

# Display the pie chart
plt.show()