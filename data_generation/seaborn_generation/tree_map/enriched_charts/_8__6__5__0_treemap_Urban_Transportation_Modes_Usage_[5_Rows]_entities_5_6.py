
import pandas as pd
import matplotlib.pyplot as plt
import squarify  # pip install squarify (algorithm for treemap)

# Create the dataframe
df = pd.DataFrame({
    'Country': ['France', 'Spain', 'USA', 'China', 'Italy', 'Turkey', 'Mexico', 'Germany', 'Thailand', 'UK', 'Japan', 'Austria', 'Greece', 'Russia', 'Portugal', 'Canada', 'India', 'Netherlands', 'Australia', 'Malaysia'],
    'Visitors': [89000, 83000, 82000, 81000, 65000, 51000, 45000, 39000, 38000, 36000, 32000, 30000, 29000, 28000, 27000, 25000, 24000, 23000, 22000, 21000]
})

# Custom colors for the treemap
colors = ['#FF6F61', '#6B5B95', '#88B04B', '#F7CAC9', '#92A8D1', '#955251', '#B565A7', '#009B77', '#DD4124', '#45B8AC', '#EFC050', '#5B5EA6', '#9B2335', '#DFCFBE', '#BC243C', '#C3447A', '#98B4D4', '#6C4F3D', '#D65076', '#E15D44']

# Create a figure and a set of subplots
plt.figure(figsize=(18, 10))

# Using squarify to plot the treemap
squarify.plot(sizes=df['Visitors'], label=df['Country'], color=colors, alpha=0.8)

plt.title("Tourist Attraction Visitors by Country", fontsize=24, fontweight='bold', pad=20)
plt.axis('off')  # Disable the axis

plt.show()