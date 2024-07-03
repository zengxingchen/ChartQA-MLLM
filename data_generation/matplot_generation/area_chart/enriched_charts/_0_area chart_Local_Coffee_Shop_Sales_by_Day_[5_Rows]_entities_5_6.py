
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'AvgTemperature': [5, 6, 10, 14, 18, 22, 25, 24, 20, 15, 10, 6]
}
df = pd.DataFrame(data)

# Convert 'Month' to categorical type with proper order
df['Month'] = pd.Categorical(df['Month'], categories=data['Month'], ordered=True)

# Create the area chart
plt.figure(figsize=(12, 8))
sns.set_theme(style="whitegrid")
area_chart = sns.lineplot(data=df, x='Month', y='AvgTemperature', sort=False, lw=1)

# Filling the area under the line
plt.fill_between(x=df['Month'], y1=df['AvgTemperature'], color='#007acc', alpha=0.5)

# Annotate the chart with text labels
for i in range(df.shape[0]):
    plt.text(df['Month'][i], df['AvgTemperature'][i]+0.5, str(df['AvgTemperature'][i])+'°C', horizontalalignment='center')

# Customize the axes
area_chart.set_xlabel('Month')
area_chart.set_ylabel('Average Temperature (°C)')
area_chart.set_title('Average Monthly Temperatures for City A (°C)')

# Show the final plot
plt.show()