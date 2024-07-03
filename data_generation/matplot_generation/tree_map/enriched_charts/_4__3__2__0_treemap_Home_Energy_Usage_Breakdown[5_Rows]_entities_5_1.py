
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Define the dataset
data = {
    'Category': ['Electricity Production', 'Transportation', 'Agriculture', 
                 'Industry', 'Residential', 'Waste Management', 
                 'Commercial', 'Forestry', 'Other'],
    'Amount': [35.7, 23.1, 18.3, 10.9, 7.6, 4.2, 8.4, 5.3, 2.5]
}

df = pd.DataFrame(data)

# Define the color scheme
colors = ['#4B0082', '#FF4500', '#32CD32', '#1E90FF', 
          '#FFD700', '#DA70D6', '#8B4513', '#5F9EA0', 
          '#D2691E']

# Create the figure with specified figure size
fig = plt.figure(figsize=(18, 14))
ax = fig.add_subplot(111, aspect="auto")

# Create a treemap
squarify.plot(sizes=df['Amount'], label=df['Category'], color=colors, alpha=0.8)

# Set the title of the plot
plt.title('Sources of Greenhouse Gas Emissions', fontsize=26)

# Remove the axes
plt.axis('off')

# Show the plot
plt.show()