
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 
              'September', 'October', 'November', 'December'],
    'Green Energy': [120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230],
    'Non-renewable Energy': [200, 210, 230, 250, 270, 290, 310, 330, 350, 370, 390, 410],
    'Hybrid Energy': [80, 85, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Wide to long format for stacking
df_long = pd.melt(df, id_vars='Month', var_name='Energy Type', value_name='Quantity')

# Transform the Month to categorical type so the order is kept in the plotting
df_long['Month'] = pd.Categorical(df_long['Month'], 
                                  categories=['January', 'February', 'March', 'April', 'May', 'June', 
                                              'July', 'August', 'September', 'October', 'November', 'December'],
                                  ordered=True)

# Set the figure size
plt.figure(figsize=(20, 12))

# Stacked area plot
sns.set_theme(style="whitegrid")
pal = ['#007acc', '#ff9900', '#33cc33']

# Plot stack area chart
ax = df.set_index('Month').plot(kind='area', stacked=True, color=pal)

# Annotate the chart with total quantity per month
df['Total'] = df['Green Energy'] + df['Non-renewable Energy'] + df['Hybrid Energy']
for idx, total in enumerate(df['Total']):
    ax.text(idx, total, str(total), va='bottom', ha='center')

# Customize title and labels
ax.set_title('Monthly Energy Consumption by Type', fontsize=20, pad=25)
ax.set_ylabel('Quantity (in units)', fontsize=16)
ax.set_xlabel('Month', fontsize=16)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Add legend
plt.legend(title='Energy Type', loc='upper left', bbox_to_anchor=(1.05, 1))

# Show the plot
plt.tight_layout()
plt.show()