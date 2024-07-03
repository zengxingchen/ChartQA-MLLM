
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Define the data
data = {
    'Country': ['USA', 'USA', 'UK', 'UK', 'Japan', 'Japan', 'Germany', 'Germany', 'France', 'France', 'Australia', 'Australia', 'Canada', 'Canada'],
    'TravelType': ['Leisure', 'Business', 'Leisure', 'Business', 'Leisure', 'Business', 'Leisure', 'Business', 'Leisure', 'Business', 'Leisure', 'Business', 'Leisure', 'Business'],
    'Travelers': [500000, 300000, 450000, 280000, 400000, 350000, 350000, 300000, 320000, 290000, 300000, 250000, 310000, 270000],
    'AvgMonthlyExpenses': [2000, 2500, 1800, 2200, 1600, 2100, 1500, 2000, 1700, 2100, 1400, 1900, 1500, 2000]
}

# Create DataFrame
df = pd.DataFrame(data)

# Create the bubble chart
plt.figure(figsize=(18, 14))
bubble_plot = sns.scatterplot(data=df, x='Country', y='AvgMonthlyExpenses', size='Travelers', hue='TravelType',
                              sizes=(100, 2000), alpha=0.7, palette=["#FF5733", "#33C1FF"])

# Customize legend and axis labels
bubble_plot.legend(title='Travel Type', loc='upper left')
plt.xlabel('Country')
plt.ylabel('Average Monthly Expenses ($)')
plt.title('Average Monthly Travel Expenses by Travel Type in Different Countries', pad=40)

# Show the plot
plt.show()