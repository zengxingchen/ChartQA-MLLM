
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 
              'September', 'October', 'November', 'December'],
    'Exercise': [3000, 3200, 3500, 3800, 4000, 4200, 4500, 4700, 4800, 5000, 5200, 5400],
    'Reading': [2500, 2700, 2900, 3100, 3300, 3500, 3700, 3900, 4000, 4200, 4400, 4600],
    'Meditation': [1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Wide to long format for stacking
df_long = pd.melt(df, id_vars='Month', var_name='Activity', value_name='Hours')

# Transform the Month to categorical type so the order is kept in the plotting
df_long['Month'] = pd.Categorical(df_long['Month'], 
                                  categories=['January', 'February', 'March', 'April', 'May', 'June', 
                                              'July', 'August', 'September', 'October', 'November', 'December'],
                                  ordered=True)

# Set the figure size
plt.figure(figsize=(14, 10))

# Stacked area plot
sns.set_theme(style="whitegrid")
pal = ['#2c7bb6', '#abd9e9', '#fdae61']

# Plot stack area chart
ax = df.set_index('Month').plot(kind='area', stacked=True, color=pal)

# Annotate the chart with total hours per month
df['Total'] = df['Exercise'] + df['Reading'] + df['Meditation']
for idx, total in enumerate(df['Total']):
    ax.text(idx, total + 100, str(total), va='bottom', ha='center', fontsize=10)

# Customize title and labels
ax.set_title('Monthly Wellness Activities Distribution', fontsize=18, pad=20)
ax.set_ylabel('Total Hours Spent', fontsize=14)
ax.set_xlabel('Month', fontsize=14)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Adjust legend position
ax.legend(loc='upper left', fontsize=12)

# Show the plot
plt.tight_layout()
plt.show()