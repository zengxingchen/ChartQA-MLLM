
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 
              'September', 'October', 'November', 'December'],
    'Electronics': [15000, 16000, 18000, 20500, 22000, 24000, 26000, 27000, 28000, 29500, 32000, 34000],
    'Fashion': [7000, 8000, 8500, 9200, 9500, 11000, 10500, 12000, 13000, 14000, 15000, 16000],
    'Home Goods': [8000, 8500, 8700, 8900, 9000, 9200, 9300, 9500, 9700, 9800, 10000, 11000]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Wide to long format for stacking
df_long = pd.melt(df, id_vars='Month', var_name='Category', value_name='Sales')

# Transform the Month to categorical type so the order is kept in the plotting
df_long['Month'] = pd.Categorical(df_long['Month'], 
                                  categories=['January', 'February', 'March', 'April', 'May', 'June', 
                                              'July', 'August', 'September', 'October', 'November', 'December'],
                                  ordered=True)

# Set the figure size
plt.figure(figsize=(12, 8))

# Stacked area plot
sns.set_theme(style="whitegrid")
pal = ['#1f77b4', '#ff7f0e', '#2ca02c']

# Plot stack area chart
ax = df.set_index('Month').plot(kind='area', stacked=True, color=pal)

# Annotate the chart with total sales per month
df['Total'] = df['Electronics'] + df['Fashion'] + df['Home Goods']
for idx, total in enumerate(df['Total']):
    ax.text(idx, total, str(total), va='bottom', ha='center')

# Customize title and labels
ax.set_title('Monthly Sales Distribution across Product Categories', fontsize=16)
ax.set_ylabel('Monthly Sales', fontsize=14)
ax.set_xlabel('Month', fontsize=14)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Show the plot
plt.tight_layout()
plt.show()