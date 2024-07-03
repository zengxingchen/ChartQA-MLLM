
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import squarify  # pip install squarify (algorithm for treemap)

# Create the dataframe
df = pd.DataFrame({
    'Topic': ['Renewable Energy', 'Climate Policy', 'Sustainable Agriculture', 'Water Conservation', 'Wildlife Protection', 
              'Ocean Cleanup', 'Air Quality Improvement', 'Green Technology', 'Reforestation', 'Eco-friendly Products', 
              'Waste Management', 'Environmental Education', 'Biodiversity Research', 'Urban Green Spaces', 
              'Carbon Footprint Reduction', 'Energy Efficiency', 'Sustainable Transportation', 'Climate Adaptation'],
    'Funding': [400, 350, 300, 250, 200, 180, 220, 260, 210, 230, 240, 190, 170, 280, 290, 310, 330, 340]
})

# Custom colors for the treemap
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', 
          '#393b79', '#637939', '#8c6d31', '#843c39', '#ad494a', '#d6616b', '#e7969c', '#7b4173']

# Create a figure and a set of subplots
plt.figure(figsize=(20, 12))

# Using squarify to plot the treemap
squarify.plot(sizes=df['Funding'], label=df['Topic'], color=colors, alpha=0.8)

plt.title("Distribution of Funding in Environment & Climate Change", fontsize=24, fontweight='bold')
plt.axis('off')  # Disable the axis

plt.show()