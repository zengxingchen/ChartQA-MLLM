
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Define the dataframe with the new topic and data points
data = {
    'Sector': ['Retail Banking', 'Corporate Banking', 'Investment Banking', 'Private Banking', 'Asset Management', 'Wealth Management', 'Mortgage Banking', 'Credit Unions', 'Online Banks', 'Others'],
    'Market Share': [25, 20, 15, 10, 8, 7, 5, 4, 3, 3]
}

df = pd.DataFrame(data)

# Define a new color list for better visual appeal
colors = ['#FF6F61', '#6B5B95', '#88B04B', '#F7CAC9', '#92A8D1', '#955251', '#B565A7', '#009B77', '#DD4124', '#45B8AC']

# Plot the treemap with modified dimensions
plt.figure(figsize=(24, 12))
squarify.plot(sizes=df['Market Share'], label=df['Sector'], color=colors, alpha=0.8)

# Add title to the plot
plt.title('Market Share of Different Banking Sectors in 2023', fontsize=24, pad=20)

# Remove axes for a cleaner look
plt.axis('off')

plt.show()