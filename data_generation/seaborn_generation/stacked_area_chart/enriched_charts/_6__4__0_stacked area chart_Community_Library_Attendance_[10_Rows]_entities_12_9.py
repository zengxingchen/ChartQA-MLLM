
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 
              'September', 'October', 'November', 'December'],
    'Online Courses': [10000, 12000, 11000, 15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000],
    'In-Person Workshops': [5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000, 16000],
    'Webinars': [15000, 14000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000, 24000, 25000]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Transform the Month to categorical type so the order is kept in the plotting
df['Month'] = pd.Categorical(df['Month'], 
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
df['Total'] = df['Online Courses'] + df['In-Person Workshops'] + df['Webinars']
for idx, total in enumerate(df['Total']):
    ax.text(idx, total, str(total), va='bottom', ha='center')

# Customize title and labels
ax.set_title('Monthly Participation in Learning Activities', fontsize=18, pad=20)
ax.set_ylabel('Number of Participants', fontsize=14)
ax.set_xlabel('Month', fontsize=14)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Add legend
plt.legend(title='Activity', loc='upper left', bbox_to_anchor=(1, 1))

# Show the plot
plt.tight_layout()
plt.show()