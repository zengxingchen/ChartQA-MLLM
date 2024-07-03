
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create the dataset
data = pd.DataFrame({
    'Age Group': ['18-25', '18-25', '26-35', '26-35', '36-45', '36-45', '46-55', '46-55', '56-65', '56-65', '66+', '66+'],
    'Exercise Time (Minutes)': [45, 50, 40, 35, 30, 25, 20, 15, 10, 8, 5, 4],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female']
})

# Set the style and color palette of the plot
sns.set_style('darkgrid')
sns.set_palette(['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#57FF33', '#FF8C33'])

# Create a vertical bar chart
plt.figure(figsize=(10, 6))  # Width and height of the chart
chart = sns.barplot(x='Age Group', y='Exercise Time (Minutes)', hue='Gender', data=data, dodge=True, saturation=0.8)

chart.set_xlabel('Age Group', fontsize=12)
chart.set_ylabel('Average Daily Exercise Time (Minutes)', fontsize=12)
chart.set_title('Average Daily Exercise Time by Age Group and Gender', fontsize=14, pad=20)

# Change the width of bars
for bar in chart.patches:
    bar.set_width(0.35)

plt.show()