
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import squarify  # pip install squarify (algorithm for treemap)

# Create the dataframe
df = pd.DataFrame({
    'Field': ['Biotechnology', 'Artificial Intelligence', 'Renewable Energy', 'Quantum Computing', 'Space Exploration',
              'Robotics', 'Climate Change', 'Material Science', 'Aerospace', 'Neuroscience', 'Data Science', 'Genomics', 'Cybersecurity',
              'Sports Science', 'Nutrition Science', 'Medical Research', 'Psychology', 'Environmental Science'],
    'Funding': [300, 250, 150, 100, 190, 130, 210, 170, 160, 90, 120, 80, 110, 140, 200, 310, 220, 180]
})

# Custom colors for the treemap
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#33FFF5', '#FF8C33', '#8C33FF', '#FF3333', '#33FF8C', '#FF5733',
          '#FF33A6', '#33FFF5', '#FF8C33', '#8C33FF', '#FF3333', '#33FF8C', '#FF33A6', '#33FFF5']

# Create a figure and a set of subplots
plt.figure(figsize=(18, 10))

# Using squarify to plot the treemap
squarify.plot(sizes=df['Funding'], label=df['Field'], color=colors, alpha=0.8)

plt.title("Distribution of Research Funding in Health & Psychology", fontsize=24, fontweight='bold')
plt.axis('off')  # Disable the axis

plt.show()