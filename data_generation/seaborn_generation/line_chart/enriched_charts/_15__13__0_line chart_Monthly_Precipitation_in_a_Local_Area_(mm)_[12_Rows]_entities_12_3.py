
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create data
data = {
    'Month': ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"],
    'Temperature Change': [0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6],
    'CO2 Emissions': [400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510],
    'Sea Level Rise': [3.2, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 4.0, 4.1, 4.2, 4.3, 4.4]
}

# Convert data into DataFrame
df = pd.DataFrame(data)

# Melt the DataFrame
df_melted = df.melt('Month', var_name='Indicator', value_name='Value')

# Create the line plot
plt.figure(figsize=(16, 8))
sns.lineplot(data=df_melted, x='Month', y='Value', hue='Indicator',
             palette=['#1f77b4', '#ff7f0e', '#2ca02c'])

# Add annotations for the start and end of each line
for indicator in ['Temperature Change', 'CO2 Emissions', 'Sea Level Rise']:
    plt.text(x=df['Month'][0], y=df[indicator][0], s=f"{df[indicator][0]} (Start)",
             color='black', ha='center', va='bottom')
    plt.text(x=df['Month'].iloc[-1], y=df[indicator].iloc[-1],
             s=f"{df[indicator].iloc[-1]} (End)", color='black', ha='center', va='bottom')

plt.title('Monthly Environmental Indicators in 2024', loc='left', fontsize=15)
plt.xlabel('Month')
plt.ylabel('Value')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()