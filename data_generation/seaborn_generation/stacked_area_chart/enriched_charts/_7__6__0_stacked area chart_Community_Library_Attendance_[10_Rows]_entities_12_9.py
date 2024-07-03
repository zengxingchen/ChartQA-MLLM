
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 
              'September', 'October', 'November', 'December'],
    'Hiking': [2800, 3000, 3500, 3700, 3900, 4200, 4500, 4700, 4800, 5100, 5300, 5500],
    'Camping': [2200, 2400, 2700, 2900, 3100, 3400, 3600, 3800, 4000, 4200, 4400, 4600],
    'Road Trips': [1600, 1800, 2000, 2200, 2400, 2600, 2800, 3000, 3200, 3400, 3600, 3800]
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
plt.figure(figsize=(16, 12))

# Stacked area plot
sns.set_theme(style="whitegrid")
pal = ['#FF6347', '#4682B4', '#3CB371']

# Plot stack area chart
ax = df.set_index('Month').plot(kind='area', stacked=True, color=pal)

# Annotate the chart with total hours per month
df['Total'] = df['Hiking'] + df['Camping'] + df['Road Trips']
for idx, total in enumerate(df['Total']):
    ax.text(idx, total + 100, str(total), va='bottom', ha='center', fontsize=10)

# Customize title and labels
ax.set_title('Monthly Adventure Activities Distribution', fontsize=20, pad=30)
ax.set_ylabel('Total Hours Spent', fontsize=16)
ax.set_xlabel('Month', fontsize=16)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Adjust legend position
ax.legend(loc='upper right', fontsize=12)

# Show the plot
plt.tight_layout()
plt.show()