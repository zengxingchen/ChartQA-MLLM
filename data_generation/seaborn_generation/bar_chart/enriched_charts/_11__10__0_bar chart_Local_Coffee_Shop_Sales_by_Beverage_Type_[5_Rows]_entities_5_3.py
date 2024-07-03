
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create the dataset
data = pd.DataFrame({
    'Category': ['Sci-Fi', 'Sci-Fi', 'Drama', 'Drama', 'Comedy', 'Comedy', 'Horror', 'Horror', 'Action', 'Action', 'Romance', 'Romance', 'Documentary', 'Documentary'],
    'Count': [150, 140, 200, 180, 250, 230, 90, 80, 300, 280, 120, 130, 60, 50],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female']
})

# Set the style and color palette of the plot
sns.set_style('whitegrid')
sns.set_palette(['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b'])

# Create a horizontal bar chart
plt.figure(figsize=(12, 8))  # Width and height of the chart
chart = sns.barplot(y='Category', x='Count', hue='Gender', data=data, dodge=True, saturation=0.7)

chart.set_ylabel('Movie Category', fontsize=12)
chart.set_xlabel('Number of Movies Watched', fontsize=12)
chart.set_title('Number of Movies Watched by Category and Gender', fontsize=14, pad=20)

# Change the height of bars
for bar in chart.patches:
    bar.set_height(0.5)

plt.show()