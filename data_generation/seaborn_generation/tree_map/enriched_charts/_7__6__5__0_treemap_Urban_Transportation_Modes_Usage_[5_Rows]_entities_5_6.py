
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import squarify  # pip install squarify (algorithm for treemap)

# Create the dataframe
df = pd.DataFrame({
    'Topic': ['Education', 'Health', 'Technology', 'Finance', 'Environment', 'Arts', 'Sports', 'Politics', 'Science', 'Travel', 'Fashion', 'History', 'Literature', 'Food', 'Entertainment', 'Business', 'Philosophy', 'Astronomy', 'Psychology', 'Archaeology'],
    'Value': [400, 350, 300, 250, 230, 220, 210, 200, 190, 180, 170, 160, 150, 140, 130, 120, 110, 100, 90, 80]
})

# Custom colors for the treemap
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#A633FF', '#33FFDD', '#FFA533', '#8D33FF', '#FF338B', '#33FFA5', '#FF8633', '#4B33FF', '#FF336B', '#A5FF33', '#338BFF', '#FFCC33', '#33A6FF', '#FF33CC', '#A633FF', '#33FFB3']

# Create a figure and a set of subplots
plt.figure(figsize=(22, 14))

# Using squarify to plot the treemap
squarify.plot(sizes=df['Value'], label=df['Topic'], color=colors, alpha=0.8)

plt.title("Value Distribution in Various Fields of Interest", fontsize=26, fontweight='bold', pad=20)
plt.axis('off')  # Disable the axis

plt.show()