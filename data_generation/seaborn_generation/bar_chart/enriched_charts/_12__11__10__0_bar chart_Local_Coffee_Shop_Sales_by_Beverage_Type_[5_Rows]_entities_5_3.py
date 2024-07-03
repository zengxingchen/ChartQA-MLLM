
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create the dataset
data = pd.DataFrame({
    'Category': ['Ancient Civilizations', 'Ancient Civilizations', 'Medieval History', 'Medieval History', 'Modern History', 'Modern History', 'Archaeological Sites', 'Archaeological Sites', 'Historical Figures', 'Historical Figures', 'World Wars', 'World Wars', 'Revolutions', 'Revolutions'],
    'Count': [170, 160, 210, 190, 240, 220, 100, 90, 260, 250, 140, 150, 80, 70],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female']
})

# Set the style and color palette of the plot
sns.set_style('whitegrid')
sns.set_palette(['#2ca02c', '#ff7f0e'])

# Create a vertical bar chart
plt.figure(figsize=(10, 12))  # Width and height of the chart
chart = sns.barplot(x='Category', y='Count', hue='Gender', data=data, dodge=True, saturation=0.7)

chart.set_xlabel('History Topic', fontsize=12)
chart.set_ylabel('Number of People Interested', fontsize=12)
chart.set_title('Interest in History Topics by Gender', fontsize=14, pad=20)

# Change the width of bars
for bar in chart.patches:
    bar.set_width(0.5)

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()