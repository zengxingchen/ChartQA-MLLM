
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Create a DataFrame from the data above.
data = {
    'Product': ['Product A', 'Product B', 'Product C', 'Product D', 'Product E', 
                'Product F', 'Product G', 'Product H', 'Product I', 'Product J', 
                'Product K', 'Product L', 'Product M'],
    'Annual Sales': [123000, 87000, 93000, 108000, 98000, 
                     81000, 113000, 102000, 76000, 135000, 
                     120000, 99000, 94500],
    'Advertising Costs': [15000, 12000, 13000, 14500, 11000, 
                          10500, 17000, 15900, 11500, 18500,
                          16000, 12800, 14000],
    'Market Share': [10, 6, 8, 9, 7, 
                     6.5, 11, 7.5, 5, 13,
                     8.5, 6.8, 7.2]
}

df = pd.DataFrame(data)

# Define the bubble chart
plt.figure(figsize=(12, 8))
bubble_chart = sns.scatterplot(data=df, x='Annual Sales', y='Advertising Costs', 
                               hue='Market Share', size='Market Share', 
                               sizes=(100, 1000), alpha=0.7, 
                               palette=["#FF5733", "#33FF57", "#3357FF", "#FF33FB"])

# Enhance legend and labels
plt.legend(scatterpoints=1, frameon=False, labelspacing=1, title='Market Share')
plt.title('Annual Sales vs. Advertising Costs by Product with Market Share', fontsize=16)
plt.xlabel('Annual Sales ($)', fontsize=12)
plt.ylabel('Advertising Costs ($)', fontsize=12)

# Create the visualization
plt.show()