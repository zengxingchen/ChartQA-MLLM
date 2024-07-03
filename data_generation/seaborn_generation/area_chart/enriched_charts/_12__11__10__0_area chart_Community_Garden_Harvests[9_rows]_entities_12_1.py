
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data preparation
data = {
    'Date': pd.date_range(start='2020-01-01', periods=24, freq='M'),
    'Observations': [50, 70, 65, 80, 90, 85, 100, 110, 95, 120, 130, 140, 160, 170, 180, 200, 210, 220, 230, 240, 250, 260, 270, 280]
}

df = pd.DataFrame(data)

# Plotting
plt.figure(figsize=(14, 10))
sns.set(style="whitegrid")

# Create the area chart
area_plot = sns.lineplot(x='Date', y='Observations', data=df, color='#ff5733', linewidth=2)
area_plot.fill_between(df['Date'], df['Observations'], color='#ff5733', alpha=0.3)

# Adding title and labels
plt.title('Monthly Telescope Observations', fontsize=18, loc='right')
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Observations', fontsize=14)

# Adding annotation
max_observation_date = df.loc[df['Observations'].idxmax(), 'Date']
max_observation_value = df['Observations'].max()
plt.annotate('Peak Observations', xy=(max_observation_date, max_observation_value),
             xytext=(max_observation_date, max_observation_value + 20),
             arrowprops=dict(facecolor='blue', arrowstyle='->'),
             fontsize=12, color='blue')

plt.tight_layout()
plt.show()