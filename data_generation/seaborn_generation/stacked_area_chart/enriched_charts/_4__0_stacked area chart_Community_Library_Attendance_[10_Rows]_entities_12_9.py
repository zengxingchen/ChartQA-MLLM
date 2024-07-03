
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 
              'September', 'October', 'November', 'December'],
    'Camping': [12000, 15000, 13000, 14000, 16000, 18000, 20000, 22000, 19000, 21000, 23000, 25000],
    'Hiking': [8000, 9000, 9500, 10000, 10500, 11000, 11500, 12000, 12500, 13000, 13500, 14000],
    'Skiing': [5000, 7000, 6000, 8000, 8500, 9000, 9500, 10000, 10500, 11000, 12000, 13000]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Wide to long format for stacking
df_long = pd.melt(df, id_vars='Month', var_name='Activity', value_name='Participants')

# Transform the Month to categorical type so the order is kept in the plotting
df_long['Month'] = pd.Categorical(df_long['Month'], 
                                  categories=['January', 'February', 'March', 'April', 'May', 'June', 
                                              'July', 'August', 'September', 'October', 'November', 'December'],
                                  ordered=True)

# Set the figure size
plt.figure(figsize=(14, 10))

# Stacked area plot
sns.set_theme(style="whitegrid")
pal = ['#4c72b0', '#dd8452', '#55a868']

# Plot stack area chart
ax = df.set_index('Month').plot(kind='area', stacked=True, color=pal)

# Annotate the chart with total participants per month
df['Total'] = df['Camping'] + df['Hiking'] + df['Skiing']
for idx, total in enumerate(df['Total']):
    ax.text(idx, total, str(total), va='bottom', ha='center')

# Customize title and labels
ax.set_title('Monthly Participation in Outdoor Activities', fontsize=18)
ax.set_ylabel('Number of Participants', fontsize=14)
ax.set_xlabel('Month', fontsize=14)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Add legend
plt.legend(title='Activity')

# Show the plot
plt.tight_layout()
plt.show()