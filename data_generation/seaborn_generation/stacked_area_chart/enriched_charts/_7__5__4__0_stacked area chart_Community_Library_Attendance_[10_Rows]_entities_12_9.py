
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 
              'September', 'October', 'November', 'December'],
    'Local Sales': [100, 120, 130, 140, 160, 170, 180, 190, 210, 220, 230, 240],
    'Online Sales': [200, 210, 250, 270, 280, 300, 320, 330, 350, 370, 390, 400],
    'International Sales': [150, 160, 180, 190, 200, 220, 230, 240, 250, 260, 270, 280]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Wide to long format for stacking
df_long = pd.melt(df, id_vars='Month', var_name='Sales Type', value_name='Sales')

# Transform the Month to categorical type so the order is kept in the plotting
df_long['Month'] = pd.Categorical(df_long['Month'], 
                                  categories=['January', 'February', 'March', 'April', 'May', 'June', 
                                              'July', 'August', 'September', 'October', 'November', 'December'],
                                  ordered=True)

# Set the figure size
plt.figure(figsize=(18, 10))

# Stacked area plot
sns.set_theme(style="whitegrid")
pal = ['#FF5733', '#33FF57', '#3357FF']

# Plot stack area chart
ax = df.set_index('Month').plot(kind='area', stacked=True, color=pal)

# Annotate the chart with total sales per month
df['Total'] = df['Local Sales'] + df['Online Sales'] + df['International Sales']
for idx, total in enumerate(df['Total']):
    ax.text(idx, total, str(total), va='bottom', ha='center')

# Customize title and labels
ax.set_title('Monthly Sales Distribution in Retail Sector', fontsize=20, pad=30)
ax.set_ylabel('Sales Amount ($)', fontsize=14)
ax.set_xlabel('Month', fontsize=14)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Add legend
plt.legend(title='Sales Type', loc='upper left', bbox_to_anchor=(1.05, 1))

# Show the plot
plt.tight_layout()
plt.show()