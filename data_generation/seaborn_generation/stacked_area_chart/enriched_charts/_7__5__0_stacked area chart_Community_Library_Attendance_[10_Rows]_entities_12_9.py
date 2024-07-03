
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 
              'September', 'October', 'November', 'December'],
    'Adventure Tourism': [12000, 13500, 15000, 17500, 19000, 21500, 23000, 24000, 25500, 27000, 28500, 30000],
    'Health Retreats': [9000, 8500, 8900, 9300, 9500, 10000, 10500, 11200, 11500, 12000, 12500, 13000],
    'Historical Sites': [8000, 8200, 8400, 8500, 8700, 8800, 9000, 9200, 9500, 9600, 9800, 10000]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Wide to long format for stacking
df_long = pd.melt(df, id_vars='Month', var_name='Category', value_name='Visits')

# Transform the Month to categorical type so the order is kept in the plotting
df_long['Month'] = pd.Categorical(df_long['Month'], 
                                  categories=['January', 'February', 'March', 'April', 'May', 'June', 
                                              'July', 'August', 'September', 'October', 'November', 'December'],
                                  ordered=True)

# Set the figure size
plt.figure(figsize=(16, 12))

# Stacked area plot
sns.set_theme(style="whitegrid")
pal = ['#3498db', '#e74c3c', '#2ecc71']

# Plot stack area chart
ax = df.set_index('Month').plot(kind='area', stacked=True, color=pal)

# Annotate the chart with total visits per month
df['Total'] = df['Adventure Tourism'] + df['Health Retreats'] + df['Historical Sites']
for idx, total in enumerate(df['Total']):
    ax.text(idx, total, str(total), va='bottom', ha='center')

# Customize title and labels
ax.set_title('Monthly Visits Distribution in Travel & Adventure', fontsize=18, pad=20)
ax.set_ylabel('Monthly Visits', fontsize=14)
ax.set_xlabel('Month', fontsize=14)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Show the legend
ax.legend(title='Category', loc='upper left', bbox_to_anchor=(1, 1))

# Show the plot
plt.tight_layout()
plt.show()