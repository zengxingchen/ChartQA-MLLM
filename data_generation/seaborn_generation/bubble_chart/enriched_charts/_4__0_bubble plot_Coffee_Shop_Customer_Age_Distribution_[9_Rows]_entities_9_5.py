
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Create a DataFrame from the data above.
data = {
    'Product': ['Health Product A', 'Health Product B', 'Health Product C', 'Health Product D', 'Health Product E', 
                'Health Product F', 'Health Product G', 'Health Product H', 'Health Product I', 'Health Product J', 
                'Health Product K', 'Health Product L', 'Health Product M'],
    'Annual Sales': [150000, 110000, 115000, 125000, 130000, 
                     95000, 105000, 145000, 120000, 135000, 
                     142000, 128000, 134000],
    'Advertising Costs': [18000, 16000, 14500, 17500, 17000, 
                          12500, 14000, 18500, 15000, 16000,
                          19000, 16500, 17500],
    'Customer Satisfaction': [9.5, 8.0, 8.5, 9.0, 9.2, 
                              7.0, 7.5, 9.4, 8.8, 9.0,
                              9.3, 8.9, 9.1]
}

df = pd.DataFrame(data)

# Define the bubble chart
plt.figure(figsize=(14, 10))
bubble_chart = sns.scatterplot(data=df, x='Annual Sales', y='Advertising Costs', 
                               hue='Customer Satisfaction', size='Customer Satisfaction', 
                               sizes=(100, 1000), alpha=0.7, 
                               palette=["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", 
                                        "#9467bd", "#8c564b", "#e377c2", "#7f7f7f",
                                        "#bcbd22", "#17becf", "#393b79", "#637939", "#8c6d31"])

# Enhance legend and labels
plt.legend(scatterpoints=1, frameon=False, labelspacing=1, title='Customer Satisfaction')
plt.title('Annual Sales vs. Advertising Costs by Health Product with Customer Satisfaction', fontsize=16, pad=20)
plt.xlabel('Annual Sales ($)', fontsize=12)
plt.ylabel('Advertising Costs ($)', fontsize=12)

# Create the visualization
plt.show()