
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Data points
data = {
    'Group': ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C', 'D', 'D', 'D'],
    'Indicator': ['GDP Growth', 'Inflation Rate', 'Unemployment Rate', 
                  'GDP Growth', 'Inflation Rate', 'Unemployment Rate',
                  'GDP Growth', 'Inflation Rate', 'Unemployment Rate', 
                  'GDP Growth', 'Inflation Rate', 'Unemployment Rate'],
    'Value': [3.5, 2.1, 5.5, 2.8, 1.9, 6.0, 4.2, 2.5, 4.0, 3.0, 2.2, 5.0],
    'Individuals': [150, 180, 130, 160, 170, 120, 200, 150, 110, 140, 165, 135]
}

# Create DataFrame
df = pd.DataFrame(data)

# Plotting
plt.figure(figsize=(16, 12))
bubble_plot = sns.scatterplot(data=df, x='Indicator', y='Value', size='Individuals',
                              sizes=(100, 1000), hue='Group',
                              palette=["#ff6347", "#4682b4", "#32cd32", "#800080"])

# Customizing the plot
bubble_plot.set_title('Economic Indicators by Group with Number of Observations', fontsize=16)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
bubble_plot.set_xlabel("Economic Indicator")
bubble_plot.set_ylabel("Value")

# Show the plot
plt.show()