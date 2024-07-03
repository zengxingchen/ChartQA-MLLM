
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame with generated data
data = {
    'Country': [
        'United States', 'China', 'Japan', 'Germany', 'India', 'United Kingdom',
        'France', 'Brazil', 'Italy', 'Canada', 'Russia', 'South Korea',
        'Spain', 'Australia', 'Mexico', 'Indonesia', 'Netherlands', 'Saudi Arabia',
        'Turkey', 'Switzerland'
    ],
    'GDP_Per_Capita': [
        62534, 10410, 40110, 46642, 2170, 42350, 41463, 8814, 35220, 46214, 11289,
        31439, 29780, 53799, 8960, 4130, 52401, 20438, 9125, 82002
    ]
}

df = pd.DataFrame(data)

# Set the style and color palette, and increase figure size
sns.set(style="whitegrid")
plt.figure(figsize=(12, 10))

# Create a horizontal bar chart
ax = sns.barplot(
    x="GDP_Per_Capita",
    y="Country",
    data=df,
    palette=[ '#3498db', '#e74c3c', '#2ecc71', '#f1c40f', '#8e44ad', '#d35400', 
              '#1abc9c', '#2c3e50', '#f39c12', '#7f8c8d', '#c0392b', '#bdc3c7', 
              '#16a085', '#2980b9', '#9b59b6', '#34495e', '#27ae60', '#95a5a6', 
              '#ecf0f1', '#55efc4']
)

# Set the width of the bars
ax.bar_label(ax.containers[0], fmt='%.0f', label_type='edge', padding=3)

# Set the title and labels of the chart
ax.set(title='GDP Per Capita by Country', xlabel='GDP Per Capita (USD)', ylabel='Country')

# Set the band width
ax.bar_label(ax.containers[0], fmt='%.0f')

# Show the plot
plt.show()