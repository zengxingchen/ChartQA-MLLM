
import matplotlib.pyplot as plt
import seaborn as sns

# Seaborn style
sns.set(style="whitegrid")

# Given data
data = [
    {'Appliance': 'Refrigerator', 'Percentage': '30%'}, 
    {'Appliance': 'HVAC System', 'Percentage': '25%'}, 
    {'Appliance': 'Water Heating', 'Percentage': '20%'}, 
    {'Appliance': 'Lighting', 'Percentage': '15%'}, 
    {'Appliance': 'Electronics', 'Percentage': '10%'}
]

# Prepare data for plotting
labels = [item['Appliance'] for item in data]
sizes = [float(item['Percentage'].strip('%')) for item in data]
colors = sns.color_palette('pastel')[:len(labels)]  # Seaborn color palette for diversity

# Create explode data to separate slices a bit
explode = [0.05] * len(labels)  # Slightly separate all slices

# Create the pie chart
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, colors=colors, explode=explode, autopct='%1.1f%%', startangle=140)

# Equal aspect ratio ensures that pie is drawn as a circle.
plt.axis('equal')  

# Title of the pie chart
plt.title('Percentage of Energy Consumption by Appliances')

# Display the plot
plt.show()