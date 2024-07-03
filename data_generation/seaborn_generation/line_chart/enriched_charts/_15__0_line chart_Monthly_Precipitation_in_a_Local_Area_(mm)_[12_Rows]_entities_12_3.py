
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create data
data = {
    'Month': ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"],
    'Average Steps': [7500, 8000, 8500, 9000, 9500, 10000, 9500, 9000, 8500, 8000, 7500, 7000],
    'Average Sleep Hours': [6.8, 7.0, 7.2, 7.1, 7.0, 6.9, 6.8, 7.0, 7.1, 7.2, 7.3, 7.4],
    'Average Calories Burned': [2200, 2100, 2300, 2400, 2500, 2600, 2550, 2500, 2400, 2300, 2200, 2100]
}

# Convert data into DataFrame
df = pd.DataFrame(data)

# Melt the DataFrame
df_melted = df.melt('Month', var_name='Health Metric', value_name='Value')

# Create the line plot
plt.figure(figsize=(14, 8))
sns.lineplot(data=df_melted, x='Month', y='Value', hue='Health Metric',
             palette=['#1f77b4', '#ff7f0e', '#2ca02c'])

# Add annotations for the start and end of each line
for metric in ['Average Steps', 'Average Sleep Hours', 'Average Calories Burned']:
    plt.text(x=df['Month'][0], y=df[metric][0], s=f"{df[metric][0]} (Start)",
             color='black', ha='center', va='bottom')
    plt.text(x=df['Month'].iloc[-1], y=df[metric].iloc[-1],
             s=f"{df[metric].iloc[-1]} (End)", color='black', ha='center', va='bottom')

plt.title('Monthly Health Metrics Overview (Units)', fontsize=16)
plt.xlabel('Month')
plt.ylabel('Metric Value')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()