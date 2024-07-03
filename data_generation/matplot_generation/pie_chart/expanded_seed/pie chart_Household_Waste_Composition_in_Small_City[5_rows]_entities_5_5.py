
import matplotlib.pyplot as plt

# Data from the provided table
data = [{'Type of Waste': 'Food and Kitchen Waste', 'Percentage(%)': 35},
        {'Type of Waste': 'Paper and Cardboard', 'Percentage(%)': 22},
        {'Type of Waste': 'Plastics', 'Percentage(%)': 12},
        {'Type of Waste': 'Glass', 'Percentage(%)': 18},
        {'Type of Waste': 'Metal', 'Percentage(%)': 13}]

# Extracting the labels and sizes from the data
labels = [entry['Type of Waste'] for entry in data]
sizes = [entry['Percentage(%)'] for entry in data]

# Define colors for each section
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0']

# Determine which section(s) to "explode" (i.e., offset from center)
explode = (0.1, 0, 0, 0, 0) # Only "explode" the 1st section (Food and Kitchen Waste)

# Start plotting the pie chart 
plt.figure(figsize=(10,7)) # Specifies the figure size
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)

# Equal aspect ratio ensures that pie is drawn as a circle.
plt.axis('equal')  

# Title of the pie chart
plt.title('Distribution of Types of Waste') 

# Display the pie chart
plt.show()