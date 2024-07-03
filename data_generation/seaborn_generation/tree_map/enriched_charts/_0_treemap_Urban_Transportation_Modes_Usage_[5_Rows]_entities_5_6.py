
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import squarify  # pip install squarify (algorithm for treemap)

# Create the dataframe
df = pd.DataFrame({
    'Field': ['Biotechnology', 'Artificial Intelligence', 'Renewable Energy', 'Quantum Computing', 'Space Exploration',
              'Robotics', 'Climate Change', 'Material Science', 'Aerospace', 'Neuroscience', 'Data Science', 'Genomics', 'Cybersecurity'],
    'Funding': [300, 250, 150, 100, 190, 130, 210, 170, 160, 90, 120, 80, 110]
})

# Custom colors for the treemap
colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#FF66B2', '#FFFF66', '#CC99FF', '#99FFFF', '#99FFCC', '#FF9966', '#66FF66', '#FF6666', '#66FFB2']

# Create a figure and a set of subplots
plt.figure(figsize=(16, 9))

# Using squarify to plot the treemap
squarify.plot(sizes=df['Funding'], label=df['Field'], color=colors, alpha=0.8)

plt.title("Distribution of Research Funding by Field", fontsize=24, fontweight='bold')
plt.axis('off')  # Disable the axis

plt.show()