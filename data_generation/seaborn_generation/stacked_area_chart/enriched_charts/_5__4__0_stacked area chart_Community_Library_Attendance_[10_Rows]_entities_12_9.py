
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 
              'September', 'October', 'November', 'December'],
    'Online Courses': [1200, 1500, 1300, 1400, 1600, 1800, 2000, 2200, 1900, 2100, 2300, 2500],
    'Webinars': [800, 900, 950, 1000, 1050, 1100, 1150, 1200, 1250, 1300, 1350, 1400],
    'Workshops': [500, 700, 600, 800, 850, 900, 950, 1000, 1050, 1100, 1200, 1300]
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
plt.figure(figsize=(16, 12))

# Stacked area plot
sns.set_theme(style="whitegrid")
pal = ['#1f77b4', '#ff7f0e', '#2ca02c']

# Plot stack area chart
ax = df.set_index('Month').plot(kind='area', stacked=True, color=pal)

# Annotate the chart with total participants per month
df['Total'] = df['Online Courses'] + df['Webinars'] + df['Workshops']
for idx, total in enumerate(df['Total']):
    ax.text(idx, total, str(total), va='bottom', ha='center')

# Customize title and labels
ax.set_title('Monthly Participation in Online Learning Activities', fontsize=18, pad=20)
ax.set_ylabel('Number of Participants', fontsize=14)
ax.set_xlabel('Month', fontsize=14)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Add legend
plt.legend(title='Activity', loc='upper left', bbox_to_anchor=(1.05, 1))

# Show the plot
plt.tight_layout()
plt.show()