
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 
              'September', 'October', 'November', 'December'],
    'Observational Astronomy': [150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260],
    'Astrophotography': [180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290],
    'Space Research': [200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Transform the data to long format for stacking
df_long = pd.melt(df, id_vars='Month', var_name='Category', value_name='Events')

# Transform the Month to categorical type so the order is kept in the plotting
df_long['Month'] = pd.Categorical(df_long['Month'], 
                                  categories=['January', 'February', 'March', 'April', 'May', 'June', 
                                              'July', 'August', 'September', 'October', 'November', 'December'],
                                  ordered=True)

# Set the figure size
plt.figure(figsize=(14, 10))

# Stacked area plot
sns.set_theme(style="whitegrid")
pal = ['#1f77b4', '#ff7f0e', '#2ca02c']

# Plot stack area chart
ax = df.set_index('Month').plot(kind='area', stacked=True, color=pal)

# Annotate the chart with total events per month
df['Total'] = df['Observational Astronomy'] + df['Astrophotography'] + df['Space Research']
for idx, total in enumerate(df['Total']):
    ax.text(idx, total, str(total), va='bottom', ha='center')

# Customize title and labels
ax.set_title('Monthly Activities in Astronomy', fontsize=20, pad=20)
ax.set_ylabel('Number of Activities', fontsize=16)
ax.set_xlabel('Month', fontsize=16)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Show the legend
ax.legend(title='Category', loc='upper left', bbox_to_anchor=(1, 1))

# Show the plot
plt.tight_layout()
plt.show()