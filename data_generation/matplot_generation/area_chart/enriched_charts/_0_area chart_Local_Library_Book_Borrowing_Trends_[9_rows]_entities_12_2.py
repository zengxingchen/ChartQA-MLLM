
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 
              'August', 'September', 'October', 'November', 'December'],
    'Temperature': [5, 7, 10, 14, 18, 22, 25, 24, 20, 15, 10, 6]
}

# Create DataFrame
df = pd.DataFrame(data)

# Convert 'Month' to a categorical type and order it correctly
months_order = ['January', 'February', 'March', 'April', 'May', 'June', 
                'July', 'August', 'September', 'October', 'November', 'December']
df['Month'] = pd.Categorical(df['Month'], categories=months_order, ordered=True)

# Plotting
plt.figure(figsize=(12, 6))
sns.set_theme(style="whitegrid")
ax = sns.lineplot(data=df, x='Month', y='Temperature', color='#1f77b4', lw=2)
ax.fill_between(df.Month, df.Temperature, color='#1f77b4', alpha=0.3)

# Adding annotation
for line in range(0, df.shape[0]):
     ax.text(df.Month[line], df.Temperature[line], df.Temperature[line], 
             horizontalalignment='center', size='small', color='black', weight='semibold')

# Customize the axes and title
ax.set_title('Monthly Average Temperatures in City XYZ', fontsize=16)
ax.set_xlabel('Month', fontsize=12)
ax.set_ylabel('Temperature (°C)', fontsize=12)
ax.set(ylim=(0, None))

# Show final result
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()