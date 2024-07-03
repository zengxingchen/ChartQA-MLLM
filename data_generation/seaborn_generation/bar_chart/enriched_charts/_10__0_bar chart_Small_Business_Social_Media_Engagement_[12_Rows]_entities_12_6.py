
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Generate the data
data = {
    'Country': ['Canada', 'United States', 'Mexico', 'Brazil', 'United Kingdom', 'Germany', 
                'France', 'Italy', 'Russia', 'China', 'India', 'Australia', 'Japan', 
                'South Korea', 'Nigeria', 'Egypt'],
    'Average_Daily_Exercise_Time': [30, 25, 45, 35, 40, 50, 55, 60, 20, 25, 40, 30, 35, 20, 50, 45]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Set the aesthetic style of the plots
sns.set_style('whitegrid')

# Create the bar chart
plt.figure(figsize=(12, 10))  # Change width and height of the chart
ax = sns.barplot(x='Country', y='Average_Daily_Exercise_Time', data=df, palette=['#1f77b4', '#ff7f0e', '#2ca02c', 
                                                                                 '#d62728', '#9467bd', '#8c564b',
                                                                                 '#e377c2', '#7f7f7f', '#bcbd22',
                                                                                 '#17becf', '#1f77b4', '#ff7f0e',
                                                                                 '#2ca02c', '#d62728', '#9467bd',
                                                                                 '#8c564b'],
                 dodge=False)

# Modify the width of bars
for bar in ax.patches:
    bar.set_width(0.5)

# Set the title
ax.set_title('Average Daily Exercise Time by Country (minutes per day)', fontsize=16)

# Rotate x-axis labels for better readability
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, horizontalalignment='right')

# Show the plot
plt.show()