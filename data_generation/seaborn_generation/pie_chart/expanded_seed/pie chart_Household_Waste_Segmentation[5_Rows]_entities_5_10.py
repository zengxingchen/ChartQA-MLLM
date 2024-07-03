
import matplotlib.pyplot as plt
import seaborn as sns

# Set Seaborn's style and color palette
sns.set(style="whitegrid")
colors = sns.color_palette('pastel')

# Given table data
data = [{'Category': 'Organic Waste', 'Percentage': 45}, 
        {'Category': 'Paper', 'Percentage': 25}, 
        {'Category': 'Plastic', 'Percentage': 12}, 
        {'Category': 'Glass', 'Percentage': 10}, 
        {'Category': 'Metal', 'Percentage': 8}]

# Extracting the 'Category' and 'Percentage' values for pie chart input
categories = [item['Category'] for item in data]
percentages = [item['Percentage'] for item in data]

# Create a pie chart
plt.figure(figsize=(8, 8))  # Set the figure size
plt.pie(percentages, labels=categories, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title('Waste Composition')  # Set the title of the pie chart
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle

# Show the plot
plt.show()