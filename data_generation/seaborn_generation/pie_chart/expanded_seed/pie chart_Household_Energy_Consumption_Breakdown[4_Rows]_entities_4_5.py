
import matplotlib.pyplot as plt
import seaborn as sns

# Set the aesthetic style of the plots
sns.set_style('whitegrid')

# Seaborn color palette to use
colors = sns.color_palette('pastel')

# Chart data
data = [
    {'Energy Use': 'Heating', 'Percentage': 45},
    {'Energy Use': 'Cooling', 'Percentage': 6},
    {'Energy Use': 'Water Heating', 'Percentage': 14},
    {'Energy Use': 'Lighting & Appliances', 'Percentage': 35}
]

# Extracting data for the pie chart
labels = [item['Energy Use'] for item in data]
sizes = [item['Percentage'] for item in data]

# Create the pie chart
plt.figure(figsize=(8, 8))  # Set the figure size
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

# Add a title
plt.title('Energy Use Distribution')

# Show the plot
plt.show()