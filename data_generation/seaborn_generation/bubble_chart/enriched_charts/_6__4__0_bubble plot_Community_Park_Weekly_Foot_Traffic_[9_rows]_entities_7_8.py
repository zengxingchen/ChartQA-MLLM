
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Define the data
data = {
    'Country': ['USA', 'USA', 'China', 'China', 'India', 'India', 'Germany', 'Germany', 'Brazil', 'Brazil', 'France', 'France', 'UK', 'UK', 'Australia', 'Australia', 'Japan', 'Japan', 'Canada', 'Canada'],
    'Topic': ['Literature', 'Writing', 'Literature', 'Writing', 'Literature', 'Writing', 'Literature', 'Writing', 'Literature', 'Writing', 'Literature', 'Writing', 'Literature', 'Writing', 'Literature', 'Writing', 'Literature', 'Writing', 'Literature', 'Writing'],
    'Participants': [100000, 90000, 150000, 95000, 120000, 110000, 80000, 60000, 50000, 55000, 55000, 50000, 70000, 75000, 65000, 62000, 130000, 115000, 90000, 85000],
    'EngagementScore': [85, 75, 90, 80, 70, 65, 78, 72, 60, 68, 82, 77, 88, 85, 81, 74, 92, 83, 80, 76]
}

# Create DataFrame
df = pd.DataFrame(data)

# Create the bubble chart
plt.figure(figsize=(18, 14))
bubble_plot = sns.scatterplot(data=df, x='Country', y='EngagementScore', size='Participants', hue='Topic',
                              sizes=(100, 2000), alpha=0.7, palette=["#FF5733", "#33FF57"])

# Customize legend and axis labels
bubble_plot.legend(title='Topic', loc='upper left')
plt.xlabel('Country')
plt.ylabel('Engagement Score')
plt.title('Engagement Score by Topic in Different Countries', pad=40)

# Show the plot
plt.show()