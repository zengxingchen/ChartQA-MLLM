
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 
              'September', 'October', 'November', 'December'],
    'Fruits': [400, 420, 450, 470, 500, 520, 550, 580, 600, 620, 640, 660],
    'Vegetables': [800, 820, 830, 840, 860, 870, 880, 890, 900, 910, 920, 930],
    'Dairy Products': [600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 700, 710]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Wide to long format for stacking
df_long = pd.melt(df, id_vars='Month', var_name='Food Category', value_name='Quantity')

# Transform the Month to categorical type so the order is kept in the plotting
df_long['Month'] = pd.Categorical(df_long['Month'], 
                                  categories=['January', 'February', 'March', 'April', 'May', 'June', 
                                              'July', 'August', 'September', 'October', 'November', 'December'],
                                  ordered=True)

# Set the figure size
plt.figure(figsize=(18, 10))

# Stacked area plot
sns.set_theme(style="whitegrid")
pal = ['#5b9bd5', '#ed7d31', '#70ad47']

# Plot stack area chart
ax = df.set_index('Month').plot(kind='area', stacked=True, color=pal)

# Annotate the chart with total quantity per month
df['Total'] = df['Fruits'] + df['Vegetables'] + df['Dairy Products']
for idx, total in enumerate(df['Total']):
    ax.text(idx, total, str(total), va='bottom', ha='center')

# Customize title and labels
ax.set_title('Monthly Consumption of Food Categories', fontsize=18, pad=20)
ax.set_ylabel('Quantity', fontsize=14)
ax.set_xlabel('Month', fontsize=14)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Add legend
plt.legend(title='Food Category', loc='upper left', bbox_to_anchor=(1.05, 1))

# Show the plot
plt.tight_layout()
plt.show()