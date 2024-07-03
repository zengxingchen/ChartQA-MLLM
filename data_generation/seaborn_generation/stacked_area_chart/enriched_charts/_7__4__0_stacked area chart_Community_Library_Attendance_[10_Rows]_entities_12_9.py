
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 
              'September', 'October', 'November', 'December'],
    'Classical': [10000, 11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000, 21000],
    'Rock': [8000, 8500, 9000, 9500, 10000, 10500, 11000, 11500, 12000, 12500, 13000, 13500],
    'Jazz': [6000, 6200, 6400, 6600, 6800, 7000, 7200, 7400, 7600, 7800, 8000, 8200]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Wide to long format for stacking
df_long = pd.melt(df, id_vars='Month', var_name='Genre', value_name='Listeners')

# Transform the Month to categorical type so the order is kept in the plotting
df_long['Month'] = pd.Categorical(df_long['Month'], 
                                  categories=['January', 'February', 'March', 'April', 'May', 'June', 
                                              'July', 'August', 'September', 'October', 'November', 'December'],
                                  ordered=True)

# Set the figure size
plt.figure(figsize=(16, 12))

# Stacked area plot
sns.set_theme(style="whitegrid")
pal = ['#1f77b4', '#ff7f0e', '#2ca02c']

# Plot stack area chart
ax = df.set_index('Month').plot(kind='area', stacked=True, color=pal)

# Annotate the chart with total listeners per month
df['Total'] = df['Classical'] + df['Rock'] + df['Jazz']
for idx, total in enumerate(df['Total']):
    ax.text(idx, total, str(total), va='bottom', ha='center')

# Customize title and labels
ax.set_title('Monthly Music Genre Listeners', fontsize=18, pad=20)
ax.set_ylabel('Number of Listeners', fontsize=14)
ax.set_xlabel('Month', fontsize=14)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Add legend
plt.legend(title='Genre', loc='upper left', bbox_to_anchor=(1, 1))

# Show the plot
plt.tight_layout()
plt.show()