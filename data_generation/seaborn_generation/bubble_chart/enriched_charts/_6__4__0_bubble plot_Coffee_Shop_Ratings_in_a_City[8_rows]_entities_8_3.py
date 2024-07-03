
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Prepare the data in a Pandas DataFrame
data = {
    'Company': ['Apple', 'Microsoft', 'Google', 'Amazon', 'Facebook', 'Tesla', 'Netflix', 'Nvidia', 'Intel', 'AMD', 'Qualcomm'],
    'Stock_Price': [145, 300, 2800, 3500, 375, 700, 500, 700, 55, 95, 130],
    'Trading_Volume': [200, 150, 100, 90, 120, 180, 80, 70, 300, 280, 250],
    'Market_Cap': [2500, 2200, 1800, 1700, 1600, 1400, 1200, 1100, 1000, 900, 850]
}
df = pd.DataFrame(data)

# Create the plot
plt.figure(figsize=(14, 8))
bubble = sns.scatterplot(data=df, x='Stock_Price', y='Trading_Volume', size='Market_Cap', hue='Company', 
                         palette=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#1f77b4'], 
                         sizes=(100, 2000), alpha=0.7, edgecolor='w', linewidth=0.5)

# Customize the axes and title
plt.title('Stock Market Analysis: Price vs. Volume Bubble Chart', fontsize=16, pad=20)
plt.xlabel('Stock Price ($)', fontsize=12)
plt.ylabel('Trading Volume (Millions)', fontsize=12)

# Adjust legend
bubble.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Companies')

# Show the bubble chart
plt.show()