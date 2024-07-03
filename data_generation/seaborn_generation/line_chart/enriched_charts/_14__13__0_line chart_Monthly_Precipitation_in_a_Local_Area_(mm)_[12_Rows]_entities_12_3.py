
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create data
data = {
    'Month': ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"],
    'Destination A': [1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300],
    'Destination B': [900, 950, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900],
    'Destination C': [1100, 1050, 1000, 950, 900, 850, 800, 750, 700, 650, 600, 550]
}

# Convert data into DataFrame
df = pd.DataFrame(data)

# Melt the DataFrame
df_melted = df.melt('Month', var_name='Destination', value_name='Tourists')

# Create the line plot
plt.figure(figsize=(16, 8))
sns.lineplot(data=df_melted, x='Month', y='Tourists', hue='Destination',
             palette=['#FF5733', '#33FF57', '#3357FF'])

# Add annotations for the start and end of each line
for destination in ['Destination A', 'Destination B', 'Destination C']:
    plt.text(x=df['Month'][0], y=df[destination][0], s=f"{df[destination][0]} (Start)",
             color='black', ha='center', va='bottom')
    plt.text(x=df['Month'].iloc[-1], y=df[destination].iloc[-1],
             s=f"{df[destination].iloc[-1]} (End)", color='black', ha='center', va='bottom')

plt.title('Monthly Tourist Visits to Destinations in 2024', loc='left', fontsize=18)
plt.xlabel('Month')
plt.ylabel('Number of Tourists')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()