
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Data points
data = {
    'Group': ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C', 'D', 'D', 'D'],
    'Indicator': ['CO2 Emissions', 'Renewable Energy Usage', 'Deforestation Rate', 
                  'CO2 Emissions', 'Renewable Energy Usage', 'Deforestation Rate',
                  'CO2 Emissions', 'Renewable Energy Usage', 'Deforestation Rate', 
                  'CO2 Emissions', 'Renewable Energy Usage', 'Deforestation Rate'],
    'Value': [88, 92, 80, 83, 87, 90, 95, 90, 85, 78, 85, 88],
    'Individuals': [150, 180, 130, 160, 170, 120, 200, 150, 110, 140, 165, 135]
}

# Create DataFrame
df = pd.DataFrame(data)

# Plotting
plt.figure(figsize=(14, 10))
bubble_plot = sns.scatterplot(data=df, x='Indicator', y='Value', size='Individuals',
                              sizes=(100, 1000), hue='Group',
                              palette=["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"])

# Customizing the plot
bubble_plot.set_title('Environmental Indicators by Group with Number of Observations', fontsize=16)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
bubble_plot.set_xlabel("Environmental Indicator")
bubble_plot.set_ylabel("Value")

# Show the plot
plt.show()