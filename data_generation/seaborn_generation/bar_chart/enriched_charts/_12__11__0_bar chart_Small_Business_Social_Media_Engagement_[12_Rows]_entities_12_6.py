
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Generate the data
data = {
    'Country': ["Iceland", "Norway", "Sweden", "Costa Rica", "Uruguay", "Denmark", 
                "Germany", "Portugal", "Spain", "Italy", "China", "India", "USA", 
                "Australia", "Canada", "Brazil"],
    'Renewable_Energy_Percentage': [85, 73, 54, 98, 97, 60, 45, 54, 40, 37, 26, 21, 11, 23, 66, 83]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Set the aesthetic style of the plots
sns.set_style('whitegrid')

# Create the bar chart
plt.figure(figsize=(12, 8))  # Change width and height of the chart
ax = sns.barplot(x='Country', y='Renewable_Energy_Percentage', data=df, palette=['#ff5733', '#33ff57', '#3357ff', 
                                                                                 '#ff33a1', '#33a1ff', '#a1ff33',
                                                                                 '#ff5733', '#33ff57', '#3357ff',
                                                                                 '#ff33a1', '#33a1ff', '#a1ff33',
                                                                                 '#ff5733', '#33ff57', '#3357ff',
                                                                                 '#ff33a1'])

# Modify the width of bars
for bar in ax.patches:
    bar.set_width(0.4)

# Set the title
ax.set_title('Renewable Energy Percentage by Country', fontsize=16, pad=20)

# Rotate x-axis labels for better readability
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')

# Show the plot
plt.show()