
import matplotlib.pyplot as plt

# Data from the given table
data = [
    {'Energy Source': 'Electricity', 'Percentage of Households': 70},
    {'Energy Source': 'Natural Gas', 'Percentage of Households': 20},
    {'Energy Source': 'Propane', 'Percentage of Households': 5},
    {'Energy Source': 'Solar', 'Percentage of Households': 3},
    {'Energy Source': 'Other', 'Percentage of Households': 2}
]

# Extracting labels and sizes for the pie chart from the data
labels = [item['Energy Source'] for item in data]
sizes = [item['Percentage of Households'] for item in data]

# Define colors for each section of the pie
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0']

# Decide to "explode" the 1st slice (Electricity)
explode = (0.1, 0, 0, 0, 0)  # Only "explode" the first slice

# Create pie chart
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
        shadow=True, startangle=90)

# Equal aspect ratio ensures that pie is drawn as a circle
ax1.axis('equal')

# Add a title to the chart
plt.title('Percentage of Households by Energy Source')

# Display the chart
plt.show()